"""
Examines scaffold hypothesis on a particular user.
Uses data from the MySQL Database.
"""
import csv
import json
import os
import numpy as np
import matplotlib.pyplot as plt
import igraph

PATH = os.path.expanduser("~/git/network_games_analysis/sql_data/")
SAVE_PATH = os.path.expanduser("~/git/network_games_analysis/scaffold/")
FILENAME = 'scaffold_data_mysql.csv'

# Specify the name of the user whose data is needed to be processed

users = ["darigan17", "Fandy", "heptone", "khana", "badhanddoek", "sittaford", "Krab", "tamas", "skillz25", "meezocool", "ThatOneGuy", "BirdEyeView", "Mursuka"]

##USER = "darigan17"
## USER = "Fandy"
## USER = "heptone"
## USER = "khana"
## USER = "badhanddoek"

def parse_data(filename, user):
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
            elif row[2] == user or user == "all":
                line_count += 1
                # user = row[2]
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


def save_graph(graph,user):
    """Saves scaffold graph in GML format"""
    igraph.save(graph, filename=SAVE_PATH + f'mysql_{user}.gml')


def main():
    # Complete analysis of the user
    # user_graph, user = parse_data(PATH + FILENAME, users[0])
    # analyse_graph(user_graph, user)
    # save_graph(user_graph,user)

    # for user in users:
    #      user_graph, user = parse_data(PATH + FILENAME, user)
    #      save_graph(user_graph,user)
        
    # user_graph, user = parse_data(PATH + FILENAME, user = "all")
    # save_graph(user_graph,user)

        
    # Load and analyse graph

    # g1 = load_graph(SAVE_PATH + f'mysql_{users[0]}.gml')
    # btwn = g1.vs["weight"]
    # ntile = np.percentile(btwn, 99.82)
    # sub_vs = g1.vs.select([v for v, b in enumerate(btwn) if b >= ntile])
    # sg1 = g1.subgraph(sub_vs)
    # g2 = load_graph(SAVE_PATH + f'mysql_{users[1]}.gml')
    # btwn = g2.vs["weight"]
    # ntile = np.percentile(btwn, 99.85)
    # sub_vs = g2.vs.select([v for v, b in enumerate(btwn) if b >= ntile])
    # sg2 = g2.subgraph(sub_vs)
    # u = igraph.union((sg1, sg2))

    vcounts = list()
    ecounts = list()
    avgDists = list()
    for index, user in enumerate(users):
        print(SAVE_PATH + f'mysql_{user}.gml')
        user_graph = load_graph(SAVE_PATH + f'mysql_{user}.gml')
        del(user_graph.es['weight'])
        if index == 0:
            union = user_graph
        else:
            comNodes = list(set(user_graph.vs['name']) & set(union.vs['name']))
            user_subgraph = user_graph.subgraph(comNodes)
            union = igraph.Graph.union(union, user_subgraph, byname = True)
        vcounts.append(union.vcount())
        ecounts.append(union.ecount())
        avgDists.append(np.mean(union.clusters().giant().shortest_paths()))
        
    plt.plot(vcounts)
    plt.plot(ecounts)
    plt.show()
    plt.plot(avgDists)
    plt.show()

if (__name__ == '__main__'):
    main()
