"""
Examines scaffold hypothesis on a particular user.
Uses data from the MySQL Database.
"""
import csv
import json
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import igraph

PATH = os.path.expanduser("~/git/network_games_analysis/sql_data/")
SAVE_PATH = os.path.expanduser("~/git/network_games_analysis/scaffold/")
FILENAME = 'scaffold_data_mysql.csv'

# Specify the name of the user whose data is needed to be processed
USER = "darigan17"
## USER = "Fandy"
## USER = "heptone"
## USER = "khana"
## USER = "badhanddoek"

def read_tag_data(tagfile = os.path.expanduser("~/git/network_games_analysis/python_scripts/tags.csv")):
    tag_df = pd.read_csv(tagfile)
    return tag_df

def get_article_tag(article, tag_df):
    tag = tag_df.loc[tag_df["Title"] == article]["Tag"]
    if len(tag) == 0:
        return("Unk")
    else:
        return tag.values[0]

def parse_data(filename, tag_df):
    """
    Parses data from a tab delimited CSV file, assembles user graph
    :param filename: Input file name
    :return: The user and its edge usage graph
    """

    with open(filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter='\t')
        print(f"Parsed file: {FILENAME}")
        line_count = 0
        user_count = 0

        user_last_clicks = {}
        user_graph = igraph.Graph()

        for row in csv_reader:
            # Ignoring header row
            if line_count == 0:
                print(f'Columns: {", ".join(row)}')
                line_count += 1
            # Ignoring data from other users
            elif row[2] == USER:
                line_count += 1
                user = row[2]
                article = row[3]
                game = row[4]

                # Add edge to the user graph
                try:
                    node = user_graph.vs.find(article)
                    node['weight'] += 1
                except ValueError:
                    user_graph.add_vertex(name=article)
                    node = user_graph.vs.find(article)
                    node['weight'] = 1
                    node['tag'] = get_article_tag(article, tag_df)
                if user_last_clicks.get('game', "") == game:
                    if user_last_clicks['article'] != article:
                        # Either add edge or increase its weight if it already exists
                        try:
                            e = user_graph.es.find(_source=user_last_clicks['article'], _target=article)
                            e['weight'] += 1
                        except ValueError:
                            user_graph.add_edge(source=user_last_clicks['article'], target=article, weight=1)

                user_last_clicks = {"article": article, "game": game}
            else:
                continue

    print(f"{user_count} users created")
    return user_graph, user

def analyse_graph(user_graph, user):
    """
    Analyses the scaffold graph of the current user.
    """
    print("Analysing user graph...")

    # Plotting degree distributions
    degree_dist = np.bincount(user_graph.degree())
    x = range(degree_dist.size)

    fig = plt.figure()
    fig.suptitle("Degree distribution")
    plt.plot(x, degree_dist, c="blue")
    plt.xlabel("Number of connections")
    plt.ylabel("Number of nodes")
    plt.xscale("log")
    plt.yscale("log")

    # plt.show()
    fig.savefig(SAVE_PATH + f"mysql_{user}_dd.png")
    plt.close(fig)

    # Creating edge weight distribution
    edge_weights = user_graph.es['weight']
    counts = np.bincount(edge_weights)
    x = range(counts.size)

    fig, ax = plt.subplots()
    ax.plot(x, counts, 'bo')
    ax.set_xlabel("Weights (Number of uses)")
    ax.set_ylabel("Occurrences (Number of edges with particular weight)")
    ax.set_title("Edge weight distribution")
    plt.yscale("log")
    plt.xscale("log")
    plt.grid()
    fig.savefig(SAVE_PATH + f"mysql_{user}_ew.png")
    # plt.show()
    plt.close(fig)

    # Creating subgraph by betweenness centrality
    #btwn = user_graph.betweenness(directed=True, weights=None)
    ## Nasty hack for using node weight instead of betweenness
    btwn = user_graph.vs["weight"]
    ntile = np.percentile(btwn, 97)
    sub_vs = user_graph.vs.select([v for v, b in enumerate(btwn) if b >= ntile])
    sub_graph = user_graph.subgraph(sub_vs)
    print(f'Generated subgraph with {sub_graph.vcount()} vertices and {sub_graph.ecount()} edges.')

    # Plotting subgraph
    # Coloring edges
    colors = ["orange", "darkorange", "red", "blue"]
    for e in sub_graph.es:
        weight = e['weight']
        if weight >= 15:
            e['color'] = colors[3]
        elif 8 <= weight < 15:
            e['color'] = colors[2]
        elif 3 <= weight < 8:
            e['color'] = colors[1]
        else:
            e['color'] = colors[0]

    # Clipping edge widths
    edge_widths = np.clip(a=sub_graph.es['weight'], a_min=4, a_max=15)
    node_weights = sub_graph.vs["weight"]
    maxw = max(node_weights)
    node_weights = np.divide(node_weights, maxw/100)
    # Styling graph
    visual_style = {"bbox": (3000, 3000), "margin": 17,
                    "vertex_color": 'grey',
                    "vertex_size": node_weights,
                    "vertex_label_size": 35,
                    "vertex_label": sub_graph.vs["name"], "edge_curved": True,
                    "edge_width": edge_widths}

    # Set the layout
    try:
        layout = sub_graph.layout("fr")
        visual_style["layout"] = layout
        save_name = f'mysql_{user}_reduced.png'
        igraph.plot(sub_graph, SAVE_PATH + save_name, **visual_style)
        print(f"Graph from {user} analysed and plotted to {save_name}")
    except MemoryError:
        print(f"Memory error. Skipping to plot {user}'s graph.")


def load_graph(filename):
    """Loads graph from file"""
    return igraph.load(filename)


def save_graph(graph):
    """Saves scaffold graph in GML format"""
    igraph.save(graph, filename=SAVE_PATH + f'mysql_{USER}.gml')


def main():
    # Complete analysis of the user
    tag_df = read_tag_data()
    user_graph, user = parse_data(PATH + FILENAME, tag_df)
    analyse_graph(user_graph, user)
    save_graph(user_graph)

    # Load and analyse graph
    # user_graph = load_graph(SAVE_PATH + f'mysql_{USER}.gml')
    # analyse_graph(user_graph, USER)


if (__name__ == '__main__'):
    main()
