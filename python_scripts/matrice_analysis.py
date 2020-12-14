"""
Examining data from the Matrice puzzle game for Android devices.
"""
import copy
import json
import igraph
import numpy as np
import matplotlib.pyplot as plt

GRAPH_FILE = "..\\matrice_graph\\matrice_graph.gml"
DATA_FILE = "..\\json_data\\matrice-36856749-export.json"
SAVE_PATH = "D:\\network_games\\matrice\\"


def read_graph(filename):
    """Reads whole graph from a file."""
    graph = igraph.load(filename)
    print(f'Loaded {filename}.')
    return graph


def load_data(filename):
    """Loads data from Firebase export."""
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        print(f'Loaded {filename}.')
        return data['games']


def analyse_data(data, graph):
    """Perform analysis"""

    players_stats = []
    average_degrees = []
    player_count = 0
    good_player_count = 0  # who played at least 35 games
    all_game_count = 0
    for player, player_games in data.items():
        print("Analysing {}'s data...".format(player))
        player_count += 1
        good_player_count += 1
        player_stats = {
            "user": player,
            "user_clicks": [],
            "shortest_clicks": [],
            "durations": []
        }
        # Creating an own copy of the Matrice graph for the player's routes
        player_graph = copy.deepcopy(graph)
        player_graph.es['weight'] = [0 for i in range(player_graph.ecount())]
        game_count = 0

        for game in player_games.values():
            clicks = game['chainLength']
            duration = game['duration']
            # Discard too long games
            if clicks > 30 or duration > 100:
                print("Discarding long game.")
                continue
            game_count += 1
            player_stats['user_clicks'].append(clicks)
            player_stats['durations'].append(duration)
            start = game['startState']
            end = game['endState']
            # Searching for shortest path
            shortest = graph.shortest_paths_dijkstra(source=start, target=end, weights=None)
            shortest = shortest[0][0]
            player_stats['shortest_clicks'].append(shortest)

            # Inserting path into the graph
            chain = game['stateChain'].split(" ")
            del chain[-1]

            for i, state in enumerate(chain):
                if i == 0:
                    continue
                try:
                    e = player_graph.es.find(_source=int(chain[i - 1]), _target=int(state))
                    e['weight'] += 1
                except ValueError:
                    print("Not existing edge found.")

        if game_count < 35:
            print("Skipping rookie player.")
            good_player_count -= 1
            continue
        all_game_count += game_count

        # Plotting graph of edge usage
        # Coloring edges
        colors = ["lightgrey", "orange", "red", "blue"]
        for e in player_graph.es:
            weight = e['weight']
            if weight >= 10:
                e['color'] = colors[3]
            elif 5 <= weight < 10:
                e['color'] = colors[2]
            elif 2 <= weight < 5:
                e['color'] = colors[1]
            else:
                e['color'] = colors[0]

        # Styling graph
        visual_style = {"bbox": (3000, 3000), "margin": 17, "vertex_color": 'grey', "vertex_size": 20,
                        "vertex_label_size": 8, "edge_curved": False, "layout": player_graph.layout("fr"),
                        "edge_width": player_graph.es['weight']}
        save_name = f'matrice_{player}.png'
        igraph.plot(player_graph, SAVE_PATH + save_name, **visual_style)
        print("Graph from {} analysed and plotted to {}".format(player, save_name))

        # Creating edge weight distribution
        edge_weights = player_graph.es['weight']
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
        fig.savefig(SAVE_PATH + f"matrice_{player}_ew.png")
        # plt.show()
        plt.close(fig)
        # Saving results
        players_stats.append(player_stats)
        with open(SAVE_PATH + 'matrice_results.json', 'w') as fp:
            json.dump(players_stats, fp, indent=2)

        # Counting average degree for player graph
        # player_graph.delete_edges(weight_eq=0)
        # avg_degree = igraph.mean(player_graph.degree())
        # average_degrees.append({"player": player, "average_degree": avg_degree, "game_count": game_count})
        # with open(SAVE_PATH + "avg_deg.json", "w") as fp:
        #    json.dump(average_degrees, fp, indent=2)

    print(f'Players: {player_count}, good players: {good_player_count}, games: {all_game_count}')


def main():
    graph = read_graph(GRAPH_FILE)
    games_data = load_data(DATA_FILE)

    analyse_data(games_data, graph)


if __name__ == '__main__':
    main()
