"""
Examines scaffold hypothesis.
Data from the PostgreSQL Database.
"""
import csv
import json

import igraph

PATH = "D:\\network_games\\"
SAVE_PATH = "D:\\network_games\\scaffold\\"
FILENAME = "scaffold_data_postgres.csv"


def parse_data(filename):
    """
    Parses data from CSV, assembles graphs by users
    :param filename: Input file name
    :return: List of users and user graphs
    """
    user_graphs = []
    users = []
    user_last_clicks = []

    with open(filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter='\t')
        print("Parsed file: {}".format(FILENAME))
        line_count = 0
        user_count = 0

        for row in csv_reader:
            line_count += 1
            user = row[5]
            article = row[2]
            game = row[3]

            # New user found
            try:
                idx = users.index(user)
            except ValueError:
                users.append(user)
                user_graphs.append(igraph.Graph())
                user_last_clicks.append({"article": article, "game": game})
                user_count += 1
                idx = len(users) - 1
                print("At line {} user {} created with index {}".format(line_count, user, idx))

            # Add edge to the users graph
            try:
                user_graphs[idx].vs.find(article)
            except ValueError:
                user_graphs[idx].add_vertex(name=article)
            if user_last_clicks[idx]['game'] == game:
                if user_last_clicks[idx]['article'] != article:
                    # Add edge or increase its weight
                    try:
                        e = user_graphs[idx].es.find(_source=user_last_clicks[idx]['article'], _target=article)
                        e['weight'] += 1
                    except ValueError:
                        user_graphs[idx].add_edge(source=user_last_clicks[idx]['article'], target=article, weight=1)

            user_last_clicks[idx] = {"article": article, "game": game}

    print("{} users created".format(user_count))
    return user_graphs, users


def analyse_graphs(user_graphs, users):
    """
    Analyses the click graphs of the users.
    """
    user_graph_data = []
    print("Analysing user graphs...")

    for i, user_graph in enumerate(user_graphs):
        nodes = user_graph.vcount()
        edges = user_graph.ecount()
        apl = user_graph.average_path_length(directed=True, unconn=True)
        diameter = user_graph.diameter(directed=True, unconn=True)
        average_deg = igraph.mean(user_graph.degree())
        # degree_dist = user_graph.degree_distribution()
        giant_component_size = max(user_graph.components().sizes())
        user_graph_data.append(
            {
                "user": users[i],
                "node_count": nodes,
                "edge_count": edges,
                "apl": apl,
                "diameter": diameter,
                "avg_degree": average_deg,
                "giant_component_size": giant_component_size
            }
        )

        colors = ["orange", "darkorange", "red", "blue"]
        for e in user_graph.es:
            weight = e['weight']
            if weight >= 15:
                e['color'] = colors[3]
            elif 8 <= weight < 15:
                e['color'] = colors[2]
            elif 3 <= weight < 8:
                e['color'] = colors[1]
            else:
                e['color'] = colors[0]

        visual_style = {"bbox": (3000, 3000), "margin": 17, "vertex_color": 'grey', "vertex_size": 20,
                        "vertex_label_size": 8, "edge_curved": False}

        # Set the layout
        try:
            layout = user_graph.layout("fr")
            visual_style["layout"] = layout
            save_name = f'postgres_{users[i]}.eps'
            igraph.plot(user_graph, SAVE_PATH + save_name, **visual_style)
            print("Graph from {} analysed and plotted to {}".format(users[i], save_name))
        except MemoryError:
            print("Memory error. Skipping to plot {}'s graph.".format(users[i]))
            continue
        # Saving results
        with open(SAVE_PATH + 'scaffold_results_mysql.json', 'w') as fp:
            json.dump(user_graph_data, fp, indent=4)


def main():
    user_graphs, users = parse_data(PATH + FILENAME)
    analyse_graphs(user_graphs, users)


if __name__ == '__main__':
    main()
