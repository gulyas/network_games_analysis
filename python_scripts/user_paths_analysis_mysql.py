"""
Examines shortest paths assumption on a particular user.
Data from the MySQL Database.
"""
import csv
import json
import numpy
import matplotlib.pyplot as plt
from datetime import datetime

import requests

PATH = "D:\\network_games\\"
SAVE_PATH = "D:\\network_games\\paths\\"
FILENAME = "paths_data_mysql2.csv"

USER = "nbobbed37"

BASE_URL = "http://localhost:5000/paths"


def parse_data(filename):
    """
    Parses data from CSV
    :param filename: Input file name
    :return:
    """
    user_stat = {"user": USER, "user_clicks": [], "shortest_clicks": [], "durations": []}

    with open(filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter='\t')
        print("Parsed file: {}".format(FILENAME))
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                print(f'Columns: {", ".join(row)}')
                line_count += 1
            else:
                line_count += 1
                if row[0] == USER:
                    click_count = row[1]
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
                        shortest_clicks = len(response["paths"][0])
                    else:
                        shortest_clicks = -1

                    user_stat['user_clicks'].append(click_count)
                    user_stat['shortest_clicks'].append(shortest_clicks)
                    user_stat['durations'].append(timediff.total_seconds())
                else:
                    continue
    return user_stat


def plot_data(user_stat):
    """Plots user stats with pyplot"""
    user_cl = user_stat["user_clicks"].reverse()
    shortest_cl = user_stat["shortest_clicks"].reverse()
    durations = user_stat["durations"].reverse()

    x = range(len(user_cl))

    fig, ax1 = plt.subplots(nrows=2, ncols=1)
    color = 'tab:red'
    ax1[0].set_xlabel('Game')
    ax1[0].set_ylabel('User clicks', color=color)
    ax1[0].plot(x, user_cl, color=color)
    ax1[0].tick_params(axis='y', labelcolor=color)

    ax2 = ax1[0].twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Shortest path clicks', color=color)  # we already handled the x-label with ax1
    ax2.plot(x, shortest_cl, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    color = 'tab:red'
    ax1[1].set_xlabel("Game")
    ax1[1].set_ylabel("Duration [s]")
    ax1[1].plot(x, durations, color=color)
    ax1[1].tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()
    fig.savefig(SAVE_PATH + f"mysql_{USER}_stats.png")


def save_data(user_stat):
    """Saves statistics in JSON format"""
    json_data = json.dumps(user_stat, indent=4)
    with open(SAVE_PATH + f'mysql_{USER}_stats.json', 'w') as fp:
        print(json_data, file=fp)


def main():
    user_stat = parse_data(PATH + FILENAME)
    plot_data(user_stat)
    save_data(user_stat)


if __name__ == '__main__':
    main()
