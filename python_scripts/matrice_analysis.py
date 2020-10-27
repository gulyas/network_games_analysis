"""
Examining data from the Matrice puzzle game for Android devices.
"""
import igraph

GRAPH_FILE = "matrice_graph.gml"
PATH = "D:\\network_games\\"


def read_graph(filename):
    return igraph.load(filename)


def parse_data(filename):
    pass


def main():
    pass


if __name__ == '__main__':
    main()
