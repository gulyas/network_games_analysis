"""
Examines scaffold hypothesis on a particular user.
Uses data from the MySQL Database.
"""
import csv
import json
import os
import numpy as np
import matplotlib.pyplot as plt
import igraph
import pathpy as pp
from scipy.stats import chi2

PATH = os.path.expanduser("~/git/network_games_analysis/sql_data/")
SAVE_PATH = os.path.expanduser("~/git/network_games_analysis/scaffold/")
FILENAME = 'scaffold_data_mysql.csv'

# Specify the name of the user whose data is needed to be processed
USER = "darigan17"
## USER = "Fandy"
## USER = "heptone"
## USER = "khana"
## USER = "badhanddoek"

path = list()
p = pp.Paths()
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
                    p.add_path(path, separator='%')
                    
                path.clear()
                path.append(article)
            user_last_clicks = {"article": article, "game": game}
        else:
            continue

hon_1 = pp.HigherOrderNetwork(p, k=1)
hon_2 = pp.HigherOrderNetwork(p, k=2, null_model=True)
hon_5 = pp.HigherOrderNetwork(p, k=5, null_model=True)

d = hon_2.degrees_of_freedom() - hon_1.degrees_of_freedom()
x = - 2 * (hon_1.likelihood(p, log=True) - hon_2.likelihood(p, log=True))
prob = 1 - chi2.cdf(x, d)

print('p-value of null hypothesis (first-order model) is {0}'.format(prob))
                        
