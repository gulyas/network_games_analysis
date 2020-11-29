"""
Plotting statistics and distributions based on the data from the Matrice game.
"""
import numpy as np
import matplotlib.pyplot as plt
import json

PATH = "D:\\network_games\\matrice\\"
FILENAME = "matrice_results.json"

USER = "kGgIUjtRccY1QxnvFPdmHB4QM542"


def parse_data(filename):
    """Loads data from file."""
    with open(filename, 'r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
        return data


def moving_average(x, w):
    """Calculates moving average"""
    return np.convolve(x, np.ones(w) / w, 'valid')


def plot_data(data):
    for player_data in data:
        # if player_data["user"] != USER:
        #    continue
        user = player_data["user"]
        user_clicks = player_data["user_clicks"]
        shortest_clicks = player_data["shortest_clicks"]
        durations = player_data["durations"]
        avg_durations = moving_average(x=durations, w=8)

        # Calculating means and standard deviations
        diffs = np.subtract(user_clicks, shortest_clicks)
        mavg = moving_average(x=diffs, w=8)
        avg_diff = np.mean(diffs)
        std_diff = np.std(diffs)
        avg_sh = np.mean(shortest_clicks)
        std_sh = np.std(shortest_clicks)
        avg_us = np.mean(user_clicks)
        std_us = np.std(user_clicks)
        print(f'User avg, std: {avg_us}, {std_us}; Shortest avg, std: {avg_sh}, {std_sh}; Diff avg, std: {avg_diff}, {std_diff}.')

        x = range(len(user_clicks))

        # Plotting path lengths and durations
        fig, (ax0, ax1) = plt.subplots(nrows=2, ncols=1)
        ax0.set_title("Length of user and shortest paths")
        ax0.set_xlabel('Game')
        ax0.set_ylabel('Number of clicks')
        ax0.plot(x, user_clicks, 'r', label='user')
        ax0.plot(x, shortest_clicks, 'b', label='shortest')
        ax0.legend()

        color = 'tab:red'
        ax1.set_title("Durations of the games")
        ax1.set_xlabel("Game")
        ax1.set_ylabel("Duration [s]")
        ax1.plot(x, durations, color=color, label='durations')
        ax1.plot(avg_durations, color='purple', label='moving average [w=8]')
        ax1.tick_params(axis='y', labelcolor=color)
        ax1.legend()

        fig.tight_layout()  # otherwise the right y-label is slightly clipped
        # plt.show()
        print(f'Plotting {user}\'s stats.')
        fig.savefig(PATH + f"matrice_{user}_length_duration.png")
        plt.close(fig)

        color = 'tab:green'
        fig, ax = plt.subplots(nrows=1, ncols=1)
        ax.set_title("Difference between user and shortest path lenghts")
        ax.set_xlabel("Game")
        ax.set_ylabel("Difference [Number of clicks]")
        ax.plot(x, diffs, color=color, label='difference')
        ax.plot(mavg, color='r', label='moving average [w=8]')
        ax.tick_params(axis='y', labelcolor=color)
        ax.legend()

        fig.tight_layout()  # otherwise the right y-label is slightly clipped
        # plt.show()
        print(f'Plotting {user}\'s stats.')
        fig.savefig(PATH + f"matrice_{user}_difference.png")
        plt.close(fig)


def main():
    data = parse_data(PATH + FILENAME)
    plot_data(data)


if __name__ == '__main__':
    main()
