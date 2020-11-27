"""
Examines shortest paths assumption on a particular user.
Data from the MySQL Database.
"""
import csv
import json
from datetime import datetime
from random import randint

import matplotlib.pyplot as plt
import requests
import igraph
import numpy as np

PATH = "D:\\network_games\\"
SAVE_PATH = "D:\\network_games\\paths\\"
FILENAME = "paths_data_mysql2.csv"

USER = "nbobbed37"

BASE_URL = "http://localhost:5000/paths"


def choose_random(list):
    """Chooses a random element from a list"""
    n = len(list)
    if n == 1:
        return list[0]
    idx = randint(0, n - 1)
    return list[idx]


def add_to_graph(graph, path):
    last_node = None
    for node in path:
        node = str(node)
        try:
            graph.vs.find(node)
        except ValueError:
            graph.add_vertex(node)
        if last_node:
            try:
                edge = graph.es.find(_source=last_node, _target=node)
                edge["weight"] += 1
            except ValueError:
                graph.add_edge(source=last_node, target=node, weight=1)
        last_node = node


def parse_data(filename):
    """
    Parses data from CSV
    :param filename: Input file name
    :return:
    """
    user_stat = {"user": USER, "user_clicks": [], "shortest_clicks": [], "durations": []}
    shortest_graph = igraph.Graph()

    with open(filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter='\t')
        print("Parsed file: {}".format(FILENAME))
        line_count = 0

        for row in csv_reader:
            # Header row
            if line_count == 0:
                print(f'Columns: {", ".join(row)}')
                line_count += 1
            else:
                line_count += 1
                # Ignoring data from other users
                if row[0] == USER:
                    click_count = int(row[1])
                    start_article = row[2]
                    goal_article = row[3]
                    start_time = datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S')
                    end_time = datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S')
                    timediff = end_time - start_time

                    # Finding shortest path
                    print(f'[Line: {line_count}] Searching shortest path between {start_article} and {goal_article}...')

                    data = {"source": start_article, "target": goal_article}
                    # data = json.dumps(data)

                    response = requests.post(BASE_URL, json=data)
                    if response.status_code == 200:
                        response = response.json()
                        paths = response["paths"]
                        try:
                            chosen_path = choose_random(paths)
                        except ValueError:
                            continue
                        add_to_graph(shortest_graph, chosen_path)
                        shortest_clicks = len(chosen_path)
                    else:
                        shortest_clicks = -1

                    # Statistics
                    user_stat['user_clicks'].append(click_count)
                    user_stat['shortest_clicks'].append(shortest_clicks)
                    user_stat['durations'].append(timediff.total_seconds())
                else:
                    continue

    return user_stat, shortest_graph


def plot_data(user_stat):
    """Plots user stats with pyplot"""
    user_cl = user_stat["user_clicks"][::-1]
    shortest_cl = user_stat["shortest_clicks"][::-1]
    durations = user_stat["durations"][::-1]
    diffs = np.subtract(user_cl, shortest_cl)
    avg = np.average(diffs)

    x = range(len(user_cl))

    fig, ax1 = plt.subplots(nrows=3, ncols=1)
    color = 'tab:red'
    ax1[0].set_title("Length of user and shortest paths")
    ax1[0].set_xlabel('Game')
    ax1[0].set_ylabel('Number of clicks')
    ax1[0].plot(x, user_cl, 'r', label='user')
    ax1[0].plot(x, shortest_cl, 'b', label='shortest')
    ax1[0].legend()

    color = 'tab:red'
    ax1[1].set_title("Durations of the games")
    ax1[1].set_xlabel("Game")
    ax1[1].set_ylabel("Duration [s]")
    ax1[1].plot(x, durations, color=color)
    ax1[1].tick_params(axis='y', labelcolor=color)

    color = 'tab:green'
    ax1[2].set_title("Difference between user and shortest path lenghts")
    ax1[2].set_xlabel("Game")
    ax1[2].set_ylabel("Difference [Number of clicks]")
    ax1[2].plot(x, diffs, color=color, label='difference')
    ax1[2].axhline(y=avg, color='r', label=f'average = {avg}')
    ax1[2].tick_params(axis='y', labelcolor=color)
    ax1[2].legend()

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()
    fig.savefig(SAVE_PATH + f"mysql_{USER}_stats.png")


def plot_graph(graph):
    """Plots graph and saves it in .eps format"""
    colors = ["orange", "darkorange", "red", "blue"]
    for e in graph.es:
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
        layout = graph.layout("kk")
        visual_style["layout"] = layout
        save_name = f'mysql_{USER}_shortest.eps'
        igraph.plot(graph, SAVE_PATH + save_name, **visual_style)
        print("Graph from {} analysed and plotted to {}".format(USER, save_name))
    except MemoryError:
        print("Memory error. Skipping to plot {}'s graph.".format(USER))


def save_data(user_stat):
    """Saves statistics in JSON format"""
    json_data = json.dumps(user_stat, indent=4)
    with open(SAVE_PATH + f'mysql_{USER}_stats.json', 'w') as fp:
        print(json_data, file=fp)


def save_graph(graph):
    """Saves shortest paths graph in GML format."""
    igraph.save(graph, filename=SAVE_PATH + f'mysql_{USER}_shortest.gml')


def main():
    user_stat, shortest_graph = parse_data(PATH + FILENAME)
    plot_data(user_stat)
    plot_graph(shortest_graph)
    save_data(user_stat)
    save_graph(shortest_graph)


if __name__ == '__main__':
    main()
