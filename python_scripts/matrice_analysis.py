"""
Examining data from the Matrice puzzle game for Android devices.
"""
import json
import igraph

GRAPH_FILE = "..\\matrice_graph\\matrice_graph.gml"
DATA_FILE = "..\\json_data\\matrice-36856749-export.json"
SAVE_PATH = "D:\\network_games\\matrice\\"


def read_graph(filename):
    """Reads whole graph from file."""
    return igraph.load(filename)


def load_data(filename):
    """Loads data from Firebase export."""
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        return data['games']


def analyse_data(data, graph):

    for player_games in data:

        for game in player_games:
            pass


def main():
    graph = read_graph(GRAPH_FILE)
    games_data = load_data(DATA_FILE)

    analyse_data(games_data, graph)


if __name__ == '__main__':
    main()
