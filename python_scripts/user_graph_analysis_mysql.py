"""
Examines scaffold hypothesis on a particular user.
Data from the MySQL Database.
"""
import csv
import json
import numpy as np
import matplotlib.pyplot as plt
import igraph

PATH = "D:\\network_games\\"
SAVE_PATH = "D:\\network_games\\scaffold\\"
FILENAME = "scaffold_data_mysql.csv"

USER = "nbobbed37"


def parse_data(filename):
    """
    Parses data from CSV, assembles graphs by users
    :param filename: Input file name
    :return: List of users and user graphs
    """

    with open(filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter='\t')
        print("Parsed file: {}".format(FILENAME))
        line_count = 0
        user_count = 0

        user_last_clicks = {}
        user_graph = igraph.Graph()

        for row in csv_reader:
            if line_count == 0:
                print(f'Columns: {", ".join(row)}')
                line_count += 1
            elif row[2] == USER:
                line_count += 1
                user = row[2]
                article = row[3]
                game = row[4]

                # Add edge to the users graph
                try:
                    user_graph.vs.find(article)
                except ValueError:
                    user_graph.add_vertex(name=article)
                if user_last_clicks.get('game', "") == game:
                    if user_last_clicks['article'] != article:
                        # Add edge or increase its weight
                        try:
                            e = user_graph.es.find(_source=user_last_clicks['article'], _target=article)
                            e['weight'] += 1
                        except ValueError:
                            user_graph.add_edge(source=user_last_clicks['article'], target=article, weight=1)

                user_last_clicks = {"article": article, "game": game}
            else:
                continue

    print("{} users created".format(user_count))
    return user_graph, user


def analyse_graphs(user_graph, user):
    """
    Analyses the click graphs of the users.
    """
    print("Analysing user graph...")

    # Creating edge weights distribution
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

    # Creating subgraph by betweenness centrality
    btwn = user_graph.betweenness(directed=True, weights=None)
    ntile = np.percentile(btwn, 90)
    sub_vs = user_graph.vs.select([v for v, b in enumerate(btwn) if b >= ntile])
    sub_graph = user_graph.subgraph(sub_vs)
    print(f'Generated subgraph with {sub_graph.vcount()} vertices and {sub_graph.ecount()} edges.')

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

    visual_style = {"bbox": (3000, 3000), "margin": 17, "vertex_color": 'grey', "vertex_size": 10,
                    "vertex_label_size": 4, "edge_curved": False}

    # Set the layout
    try:
        layout = sub_graph.layout("fr")
        visual_style["layout"] = layout
        save_name = f'mysql_{user}_reduced.eps'
        igraph.plot(sub_graph, SAVE_PATH + save_name, **visual_style)
        print("Graph from {} analysed and plotted to {}".format(user, save_name))
    except MemoryError:
        print("Memory error. Skipping to plot {}'s graph.".format(user))


def main():
    user_graphs, users = parse_data(PATH + FILENAME)
    analyse_graphs(user_graphs, users)


if __name__ == '__main__':
    main()
