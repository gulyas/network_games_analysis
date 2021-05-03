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
import seaborn as sns
from scipy.stats import pearsonr
sns.set(style='white', font_scale=1.2)

PATH = os.path.expanduser("~/git/network_games_analysis/sql_data/")
SAVE_PATH = os.path.expanduser("~/git/network_games_analysis/scaffold/")
FILENAME = 'scaffold_data_mysql.csv'

users = ["darigan17", "Fandy", "heptone", "khana", "badhanddoek", "sittaford", "Krab", "tamas", "skillz25", "meezocool", "ThatOneGuy", "BirdEyeView", "Mursuka"]
users_short = ["darigan17", "Fandy", "heptone"]


def listrun(pattern, values):
    """Find runs in a pattern containing elements from given values"""
    runs = list()
    run = list()
    for i in pattern:
        if i in values:
            run.append(i)
        else:
            if len(run) > 1:
                runs.append(run)
                run = list()
            elif len(run) == 1:
                run = list()
    if len(run) > 1:
        runs.append(run)
    return runs

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
                
def estimate_user_kopt(user, top_nodes):

    USER = user

    ##PATH COLLECTION

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
    #print(flat_list)
    sorted_nodes=[ x[0] for x in sorted( flat_list.items() , key=lambda x: x[1], reverse=True)]
    top_sorted_nodes=sorted_nodes[0:top_node_number]
    #print(top_sorted_nodes, end="\n\n")

    paths_reduced = list()
    for path in paths:
        runs = listrun(path, top_sorted_nodes)
        for run in runs:
            paths_reduced.append(run)
    #print(paths_reduced)

    ## Add paths to pathpy 
    p = pp.Paths()
    for path in paths_reduced:
        p.add_path(path)
    print(p)
                        
    mog = pp.MultiOrderModel(p, max_order=2)
    #print('Optimal order = ', mog.estimate_order())
    return (len(paths_reduced), mog.estimate_order())


user_list = get_users()
kopts = list()
pathnums = list()
for user in user_list:
    pathnum,kopt = estimate_user_kopt(user, 25)
    kopts.append(kopt)
    pathnums.append(pathnum)
    print('Optimal orders = ', kopts)
    print(len(kopts))

# plt.plot(kopts)
# plt.plot(pathnums)
# plt.show()

eval_list = (pathnums,kopts)
df = DataFrame(eval_list).transpose()
df.columns = ['Number_of_paths','K_opt']

g = sns.JointGrid(data=df, x='Number_of_paths', y='K_opt', xlim=(0, 1000), ylim=(0, 3), height=5)
g = g.plot_joint(sns.regplot, color="xkcd:muted blue")
g = g.plot_marginals(sns.distplot, kde=False, bins=12, color="xkcd:bluey grey")
g.ax_joint.text(500, 2.8, 'r = 0.45, p < .001', fontstyle='italic')
plt.tight_layout()
plt.show()
###########################################################     Unused pathpy code

# path = ('a','b','c','d','e','c','b','a','c','d','e','c','e','d','c','a')
# p = pp.Paths()
# p.add_path(path)
# pp.visualisation.plot(pp.Network.from_paths(p))

# p = pp.Paths()
# p.add_path('a,c,d', 2)
# p.add_path('b,c,e', 2)
# print(p)
# p *= 10
##PATH ANALYSIS

#p = pp.Paths()
#p.add_path(path, separator='%')

# print("Hon1")
# hon_1 = pp.HigherOrderNetwork(p, k=1)
# print("Hon2")
# hon_2 = pp.HigherOrderNetwork(p, k=2, null_model=False)
# print("Hon3")
# hon_3 = pp.HigherOrderNetwork(p, k=3, null_model=False)
# print("Hon4")
# hon_4 = pp.HigherOrderNetwork(p, k=4, null_model=False)
# print("Hon5")
# hon_5 = pp.HigherOrderNetwork(p, k=5, null_model=False)
# print("Done")

# d = hon_4.degrees_of_freedom() - hon_3.degrees_of_freedom()
# x = - 2 * (hon_3.likelihood(p, log=True) - hon_4.likelihood(p, log=True))
# prob = 1 - chi2.cdf(x, d)

# print('p-value of null hypothesis (first-order model) is {0}'.format(prob))


# d = mog.degrees_of_freedom(max_order=2) - mog.degrees_of_freedom(max_order=1)
# x = - 2 * (mog.likelihood(p, log=True, max_order=1) 
#    - mog.likelihood(p, log=True, max_order=2))
# prob = 1 - chi2.cdf(x, d)

# print('p value of null hypothesis that data has maximum order 1 = {0}'.format(prob))

# mog.estimate_order()
