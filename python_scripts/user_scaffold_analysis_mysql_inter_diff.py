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

users = ["darigan17", "Fandy", "heptone", "khana", "badhanddoek", "sittaford", "Krab", "tamas", "skillz25", "meezocool", "ThatOneGuy", "BirdEyeView", "Mursuka"]
users_short = ["tamas", "Mursuka"]

def load_graph(filename):
    """Loads graph from file"""
    return igraph.load(filename)

def save_graph(graph,user):
    """Saves scaffold graph in GML format"""
    igraph.save(graph, filename=SAVE_PATH + f'mysql_{user}.gml')

def stats_on_unions(users):
    """Plots some basic statistics based on the union of user scaffolds"""
    vcounts = list()
    ecounts = list()
    avgDists = list()
    for index, user in enumerate(users):
        print(SAVE_PATH + f'mysql_{user}.gml')
        user_graph = load_graph(SAVE_PATH + f'mysql_{user}.gml')
        del(user_graph.es['weight'])
        if index == 0:
            union = user_graph
        else:
            comNodes = list(set(user_graph.vs['name']) & set(union.vs['name']))
            user_subgraph = user_graph.subgraph(comNodes)
            union = igraph.Graph.union(union, user_subgraph, byname = True)
        vcounts.append(union.vcount())
        ecounts.append(union.ecount())
        avgDists.append(np.mean(union.clusters().giant().shortest_paths()))

    f, (ax1, ax2) = plt.subplots(2)
    ax1.plot(vcounts)
    ax1.plot(ecounts)
    ax1.set_title('Vertex and edge counts after unions')
    ax2.plot(avgDists)
    ax2.set_title('Average distance after unions')
    plt.show()

def stats_on_intersections(users):
    """Plots some basic statistics based on the intersection of user scaffolds"""
    vcounts = list()
    ecounts = list()
    for index, user in enumerate(users):
        print(SAVE_PATH + f'mysql_{user}.gml')
        user_graph = load_graph(SAVE_PATH + f'mysql_{user}.gml')
        del(user_graph.es['weight'])
        if index == 0:
            inter = user_graph
        else:
            igraph.summary(inter)
            inter = igraph.Graph.intersection(inter, user_graph, byname = True)
            igraph.summary(inter)
            inter = inter.clusters().giant()
            igraph.summary(inter)
        vcounts.append(inter.vcount())
        ecounts.append(inter.ecount())

    # Styling graph
    visual_style = {"bbox": (1000, 1000), "margin": 77,
                    "vertex_color": 'grey',
                    "vertex_label_size": 25,
                    "vertex_label": inter.vs["name"], "edge_curved": True}
    igraph.plot(inter, **visual_style)
        
    with open('intersection_nodes.txt', 'w') as filehandle:
        for listitem in vcounts:
            filehandle.write('%s\n' % listitem)
    with open('intersection_edges.txt', 'w') as filehandle:
        for listitem in ecounts:
            filehandle.write('%s\n' % listitem)

    plt.semilogy(vcounts)
    plt.plot(ecounts)
    plt.show()

def stats_on_jaccards(users):
    """Plots some basic statistics based on the jaccard index of user scaffolds"""
    jaccards = list()
    for user1 in users:
        for user2 in users:
            if user1 == user2:
                continue
            else:
                user_graph1 = load_graph(SAVE_PATH + f'mysql_{user1}.gml')
                user_graph2 = load_graph(SAVE_PATH + f'mysql_{user2}.gml')
                del(user_graph1.es['weight'])
                del(user_graph2.es['weight'])
                inter = igraph.Graph.intersection(user_graph1, user_graph2, byname = True)
                union = igraph.Graph.union(user_graph1, user_graph2, byname = True)
                jaccard = inter.ecount() / union.ecount()
                jaccards.append(jaccard)

    print(jaccards)
    with open('jaccards.txt', 'w') as filehandle:
        for listitem in jaccards:
            filehandle.write('%s\n' % listitem)
    plt.boxplot(jaccards)
    plt.show()

def main():

    all_users = list()

    with open('users.txt', 'r') as filehandle:
        for line in filehandle:
            currentPlace = line[:-1]
            all_users.append(currentPlace)

    #print(all_users)
    # g1 = load_graph(SAVE_PATH + f'mysql_{users[0]}.gml')
    # btwn = g1.vs["weight"]
    # ntile = np.percentile(btwn, 99.82)
    # sub_vs = g1.vs.select([v for v, b in enumerate(btwn) if b >= ntile])
    # sg1 = g1.subgraph(sub_vs)
    # g2 = load_graph(SAVE_PATH + f'mysql_{users[1]}.gml')
    # btwn = g2.vs["weight"]
    # ntile = np.percentile(btwn, 99.85)
    # sub_vs = g2.vs.select([v for v, b in enumerate(btwn) if b >= ntile])
    # sg2 = g2.subgraph(sub_vs)
    # u = igraph.union((sg1, sg2))

    #stats_on_unions(users)
    #stats_on_intersections(users_short)
    stats_on_jaccards(all_users)
    
if (__name__ == '__main__'):
    main()
