"""
Extracts path data for a user or a set of users and analyses with pathpy.
"""
import csv
import json
import os
import numpy as np
import matplotlib.pyplot as plt
import igraph
import pathpy as pp
from scipy.stats import chi2
from collections import Counter
from pandas import DataFrame
import pandas as pd
import seaborn as sns
from scipy.stats import pearsonr
sns.set(style='white', font_scale=1.2)

PATH = os.path.expanduser("~/git/network_games_analysis/sql_data/")
SAVE_PATH = os.path.expanduser("~/git/network_games_analysis/scaffold/")
FILENAME = 'scaffold_data_mysql.csv'

users = ["darigan17", "Fandy", "heptone", "khana", "badhanddoek", "sittaford", "Krab", "tamas", "skillz25", "meezocool", "ThatOneGuy", "BirdEyeView", "Mursuka"]
users_short = ["darigan17", "Fandy", "heptone"]

def extract_top_articles(user, top_nodes):

    USER = user

    paths = list()
    path = list()
    filename = PATH + FILENAME
    with open(filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter='\t')
        print(f"Parsed file: {FILENAME}")
        line_count = 0
        user_count = 0
    
        user_last_clicks = {}
        for row in csv_reader:
            # Ignoring header row
            if line_count == 0:
                print(f'Columns: {", ".join(row)}')
                line_count += 1
                # Ignoring data from other users
            elif USER == "all":
                line_count += 1
                user = row[2]
                article = row[3]
                game = row[4]
          
                if user_last_clicks.get('game', "") == game:
                    if user_last_clicks['article'] != article:
                        path.append(article)
                else:
                    if len(path) != 0:
                        paths.append(path)
                    
                    path = list()
                    path.append(article)
                user_last_clicks = {"article": article, "game": game}               
            elif row[2] == USER:
                line_count += 1
                user = row[2]
                article = row[3]
                game = row[4]
          
                if user_last_clicks.get('game', "") == game:
                    if user_last_clicks['article'] != article:
                        path.append(article)
                else:
                    if len(path) != 0:
                        paths.append(path)
                    
                    path = list()
                    path.append(article)
                user_last_clicks = {"article": article, "game": game}
            else:
                continue

    ##PATH FILTERING

    top_node_number=top_nodes
    flat_list=Counter([item for path in paths for item in path])
    sorted_nodes=[ x[0] for x in sorted( flat_list.items() , key=lambda x: x[1], reverse=True)]
    top_sorted_nodes=sorted_nodes[0:top_node_number]
    return top_sorted_nodes

def save_top_nodes(top_nodes):
    titles = extract_top_articles("all", top_nodes)
    tags = ['Unk' for i in range(len(titles))]
    dict = {'Title': titles, 'Tag': tags}  
    df = DataFrame(dict) 
    df.to_csv('Top_titles.csv', index = False)


def read_tag_data(tagfile = os.path.expanduser("~/git/network_games_analysis/python_scripts/tags.csv")):
    tag_df = pd.read_csv(tagfile)
    return tag_df

def tag_analysis(user):

    USER = user

    paths = list()
    path = list()
    filename = PATH + FILENAME
    with open(filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter='\t')
        print(f"Parsed file: {FILENAME}")
        line_count = 0
        user_count = 0
    
        user_last_clicks = {}
        for row in csv_reader:
            # Ignoring header row
            if line_count == 0:
                print(f'Columns: {", ".join(row)}')
                line_count += 1
                # Ignoring data from other users
            elif USER == "all":
                line_count += 1
                user = row[2]
                article = row[3]
                game = row[4]
          
                if user_last_clicks.get('game', "") == game:
                    if user_last_clicks['article'] != article:
                        path.append(article)
                else:
                    if len(path) != 0:
                        paths.append(path)
                    
                    path = list()
                    path.append(article)
                user_last_clicks = {"article": article, "game": game}               
            elif row[2] == USER:
                line_count += 1
                user = row[2]
                article = row[3]
                game = row[4]
          
                if user_last_clicks.get('game', "") == game:
                    if user_last_clicks['article'] != article:
                        path.append(article)
                else:
                    if len(path) != 0:
                        paths.append(path)
                    
                    path = list()
                    path.append(article)
                user_last_clicks = {"article": article, "game": game}
            else:
                continue

    tag_df = read_tag_data()
    tag_list = list()
    for path in paths:
        for node in path:
            #print(node)
            tag = tag_df.loc[tag_df["Title"] == node]["Tag"]
            #print(tag)
            if len(tag) == 0:
                tag_list.append("Unk")
                #print("UNK")
            else:
                #print("else")
                tag_list.append(tag.values[0])
    return(tag_list)

def main():
    all_users = list()

    with open('users.txt', 'r') as filehandle:
        for line in filehandle:
            currentPlace = line[:-1]
            all_users.append(currentPlace)

    for user in users_short:
        print(user)
        taglist = tag_analysis(user)
        print(Counter(taglist))

        #save_top_nodes(5000)


if (__name__ == '__main__'):
    main()
