"""
Examines scaffold hypothesis on a particular user.
Uses data from the MySQL Database.
"""
import csv
import json
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import igraph

PATH = os.path.expanduser("~/git/network_games_analysis/sql_data/")
SAVE_PATH = os.path.expanduser("~/git/network_games_analysis/scaffold/")
FILENAME = 'scaffold_data_mysql.csv'

# Specify the name of the user whose data is needed to be processed

def read_tag_data(tagfile = os.path.expanduser("~/git/network_games_analysis/python_scripts/tags.csv")):
    tag_df = pd.read_csv(tagfile)
    return tag_df

def get_article_tag(article, tag_df):
    tag = tag_df.loc[tag_df["Title"] == article]["Tag"]
    if len(tag) == 0:
        return("Unk")
    else:
        return tag.values[0]


def get_users():

    users = list()

    ##PATH COLLECTION

    filename = PATH + FILENAME
    with open(filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter='\t')
        print(f"Parsed file: {FILENAME}")
        line_count = 0
        user_count = 0
        
        for row in csv_reader:
            # Ignoring header row
            if line_count == 0:
                print(f'Columns: {", ".join(row)}')
                line_count += 1
                # Ignoring data from other users
            else:
                line_count += 1
                user = row[2]
                if user not in users:
                    users.append(user)
    return users

def parse_data(filename, user, tag_df):
    """
    Parses data from a tab delimited CSV file, assembles user graph
    :param filename: Input file name
    :return: The user and its edge usage graph
    """

    with open(filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter='\t')
        print(f"Parsed file: {FILENAME}")
        line_count = 0
        user_count = 0

        user_last_clicks = {}
        user_graph = igraph.Graph()

        for row in csv_reader:
            # Ignoring header row
            if line_count == 0:
                print(f'Columns: {", ".join(row)}')
                line_count += 1
            # Ignoring data from other users
            elif row[2] == user or user == "all":
                line_count += 1
                # user = row[2]
                article = row[3]
                game = row[4]

                # Add edge to the user graph
                try:
                    node = user_graph.vs.find(article)
                    node['weight'] += 1
                except ValueError:
                    user_graph.add_vertex(name=article)
                    node = user_graph.vs.find(article)
                    node['weight'] = 1
                    node['tag'] = get_article_tag(article, tag_df)                    
                if user_last_clicks.get('game', "") == game:
                    if user_last_clicks['article'] != article:
                        # Either add edge or increase its weight if it already exists
                        try:
                            e = user_graph.es.find(_source=user_last_clicks['article'], _target=article)
                            e['weight'] += 1
                        except ValueError:
                            user_graph.add_edge(source=user_last_clicks['article'], target=article, weight=1)

                user_last_clicks = {"article": article, "game": game}
            else:
                continue

    print(f"{user_count} users created")
    return user_graph, user

def save_graph(graph,user):
    """Saves scaffold graph in GML format"""
    igraph.save(graph, filename=SAVE_PATH + f'mysql_{user}.gml')

def save_user_graphs(users, tag_df):
    """Saves scaffold graph in GML format for a list of users"""
    for user in users:
         user_graph, user = parse_data(PATH + FILENAME, user, tag_df)
         save_graph(user_graph,user)


def main():

    # Generate graph for all
    tag_df = read_tag_data()
    user_graph, user = parse_data(PATH + FILENAME, "all", tag_df)
    save_graph(user_graph,user)
    
    # all_users = get_users()
    # all_users.remove("yizikes")
    # all_users.remove("Rachel228")
    # all_users.remove("bavnah")
    # all_users.remove("Joe1234")
    # all_users.remove("alex_icon")
    # all_users.remove("SonicBoomSensei")
    # all_users.remove("SpatenOptimator")
    # all_users.remove("Rhinowire")
    # all_users.remove("beastly")
    # # Dump user names 
    # with open('users.txt', 'w') as filehandle:
    #     for listitem in all_users:
    #         filehandle.write('%s\n' % listitem)
    # save_user_graphs(all_users, tag_df)

    
if (__name__ == '__main__'):
    main()
