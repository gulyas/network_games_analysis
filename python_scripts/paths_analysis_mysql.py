"""
Examines shortest paths assumption.
Data from the MySQL Database.
"""
import csv
import json
from .wikiracer import check_pages, find_shortest_path, redirected

PATH = "D:\\network_games\\"
FILENAME = "paths_data_mysql.csv"
EXPORT_FILE_NAME = "paths_stats.json"

BASE_URL = "https://en.wikipedia.org/wiki/"

LAST_READ_LINES = 0


def parse_data(filename):
    """
    Parses data from CSV
    :param filename: Input file name
    :return:
    """
    users = []
    user_stats = []
    global_stats = {
        "user_clicks": [],
        "shortest_clicks": [],
        "durations": []
    }

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
                continue
            else:
                line_count += 1
                user = row[0]
                click_count = row[1]
                start_article = row[2]
                goal_article = row[3]
                start_time = row[5]
                end_time = row[6]

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
                start_url = BASE_URL + start_article
                goal_url = BASE_URL + goal_article
                if check_pages(start_url, goal_url):
                    result = find_shortest_path(start_url, redirected(goal_url))
                    shortest_clicks = len(result['path'])

                user_stats[idx]['user_clicks'].append(click_count)
                user_stats[idx]['shortest_clicks'].append(shortest_clicks)
                user_stats[idx]['durations'].append(timediff)  # TODO

                global_stats['user_clicks'].append(click_count)
                global_stats['shortest_clicks'].append(shortest_clicks)
                global_stats['durations'].append(timediff)

    return users, user_stats


def save_data(users, user_stats, global_stats):
    data = {
        "users": users,
        "user_stats": user_stats,
        "global_stats": global_stats
    }
    json_data = json.dumps(data, indent=4)
    with open(EXPORT_FILE_NAME, 'w') as fp:
        print(json_data, file=fp)


def main():
    users, user_stats = parse_data(PATH + FILENAME)


if __name__ == '__main__':
    main()
