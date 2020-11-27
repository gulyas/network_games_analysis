"""
Examines shortest paths assumption.
Data from the MySQL Database.
"""
import csv
import json
from datetime import datetime

import requests

PATH = "D:\\network_games\\"
SAVE_PATH = "D:\\network_games\\paths\\"
FILENAME = "paths_data_mysql2.csv"
EXPORT_FILE_NAME = "paths_stats.json"

BASE_URL = "http://localhost:5000/paths"

LAST_READ_LINES = 16750


def load_stats(filename):
    """
    Loads statistics.
    :param filename: File to be loaded.
    :return: users, user_stats, global_stats arrays
    """
    with open(filename, 'r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
        return data["users"], data["user_stats"], data["global_stats"]


def parse_data(filename, users, user_stats, global_stats):
    """
    Parses data from CSV
    :param global_stats: Global stats
    :param user_stats: Array of user stats
    :param users: Array of users
    :param filename: Input file name
    :return:
    """

    with open(filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter='\t')
        print("Parsed file: {}".format(FILENAME))
        line_count = 0
        user_count = 0

        for row in csv_reader:
            if line_count == 0:
                print(f'Columns: {", ".join(row)}')
                line_count += 1
            elif line_count <= LAST_READ_LINES:
                line_count += 1
                continue
            else:
                line_count += 1
                user = row[0]
                click_count = row[1]
                start_article = row[2]
                goal_article = row[3]
                start_time = datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S')
                end_time = datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S')
                timediff = end_time - start_time

                # New user found
                try:
                    idx = users.index(user)
                except ValueError:
                    users.append(user)
                    user_stats.append({"user_clicks": [], "shortest_clicks": [], "durations": []})
                    user_count += 1
                    idx = len(users) - 1
                    print("At line {} user {} created with index {}".format(line_count, user, idx))
                    save_data(users, user_stats, global_stats)

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

                user_stats[idx]['user_clicks'].append(click_count)
                user_stats[idx]['shortest_clicks'].append(shortest_clicks)
                user_stats[idx]['durations'].append(timediff.total_seconds())

                global_stats['user_clicks'].append(click_count)
                global_stats['shortest_clicks'].append(shortest_clicks)
                global_stats['durations'].append(timediff.total_seconds())

    return users, user_stats


def save_data(users, user_stats, global_stats):
    """Saves statistics in JSON format"""
    data = {
        "users": users,
        "user_stats": user_stats,
        "global_stats": global_stats
    }
    json_data = json.dumps(data, indent=4)
    with open(SAVE_PATH + EXPORT_FILE_NAME, 'w') as fp:
        print(json_data, file=fp)


def main():
    users, user_stats, global_stats = load_stats(SAVE_PATH + EXPORT_FILE_NAME)
    parse_data(PATH + FILENAME, users, user_stats, global_stats)


if __name__ == '__main__':
    main()
