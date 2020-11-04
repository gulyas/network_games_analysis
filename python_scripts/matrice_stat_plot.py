"""
Plotting statistics and distributions based on the data from the Matrice game.
"""
import numpy as np
import matplotlib.pyplot as plt
import json

PATH = "D:\\network_games\\matrice\\"
FILENAME = "matrice_results.json"


def parse_data(filename):
    """Loads data from file."""
    with open(filename, 'r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
        return data


def plot_data(data):
    for player_data in data:
        user = player_data["user"]
        user_clicks = player_data["user_clicks"]
        shortest_clicks = player_data["shortest_clicks"]
        durations = player_data["durations"]

        diffs = np.subtract(user_clicks, shortest_clicks)
        avg = np.average(diffs)

        x = range(len(user_clicks))

        fig, ax1 = plt.subplots(nrows=3, ncols=1)
        color = 'tab:red'
        ax1[0].set_title("Length of user and shortest paths")
        ax1[0].set_xlabel('Game')
        ax1[0].set_ylabel('Number of clicks')
        ax1[0].plot(x, user_clicks, 'r', label='user')
        ax1[0].plot(x, shortest_clicks, 'b', label='shortest')
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
        # plt.show()
        print(f'Plotting {user}\'s stats.')
        fig.savefig(PATH + f"matrice_{user}_stats.png")
        plt.close(fig)


def main():
    data = parse_data(PATH + FILENAME)
    plot_data(data)


if __name__ == '__main__':
    main()
