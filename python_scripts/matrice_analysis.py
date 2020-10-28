"""
Examining data from the Matrice puzzle game for Android devices.
"""
import copy
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
    for player, player_games in data.items():
        print("Analysing {}'s data...".format(player))
        player_stats = {
            "user_clicks": [],
            "shortest_clicks": [],
            "durations": []
        }
        player_graph = copy.deepcopy(graph)
        player_graph.es['weight'] = [0 in range(player_graph.ecount())]

        for game in player_games.values():
            player_stats['user_clicks'].append(game['chainLength'])
            player_stats['durations'].append(game['duration'])
            start = game['startState']
            end = game['endState']
            shortest = graph.shortest_paths_dijkstra(source=start, target=end, weights=None)
            player_stats['shortest_clicks'].append(shortest)
            chain = game['stateChain'].split(" ")
            del chain[-1]

            for i, state in enumerate(chain):
                if i == 0:
                    continue
                e = player_graph.es.find(source=chain[i - 1], target=state)
                e['weight'] += 1

        # Plotting graph
        colors = ["orange", "darkorange", "red", "blue"]
        for e in player_graph.es:
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
                        "vertex_label_size": 8, "edge_curved": False, "layout": player_graph.layout("kk")}

        save_name = f'matrice_{player}.eps'
        igraph.plot(player_graph, SAVE_PATH + save_name, **visual_style)
        print("Graph from {} analysed and plotted to {}".format(player, save_name))
        # Saving results
        with open(SAVE_PATH + 'matrice_results.json', 'a') as fp:
            json.dump(player_stats, fp, indent=4)


def main():
    graph = read_graph(GRAPH_FILE)
    games_data = load_data(DATA_FILE)

    analyse_data(games_data, graph)


if __name__ == '__main__':
    main()
