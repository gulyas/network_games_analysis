"""
Examining data from the Matrice puzzle game for Android devices.
"""
import json
import igraph

GRAPH_FILE = "..\\matrice_graph\\matrice_graph.gml"
DATA_FILE = "..\\json_data\\matrice-36856749-export.json"
PATH = "D:\\network_games\\"


def read_graph(filename):
    return igraph.load(filename)


def parse_data(filename):
    data = {}
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        player_games = data["games"]

        for player in player_games:

            for game in player:
                pass


def main():
    graph = read_graph(GRAPH_FILE)
    parse_data(DATA_FILE)


if __name__ == '__main__':
    main()
