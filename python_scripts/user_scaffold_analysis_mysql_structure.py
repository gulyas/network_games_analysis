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

SAVE_PATH = os.path.expanduser("~/git/network_games_analysis/scaffold_statistics/")
LOAD_PATH = os.path.expanduser("~/git/network_games_analysis/scaffold/")

def plot_scaffold_distributions(scaffold, user):
    """
    Analyses the degree distribution and edge weight distribution.
    """
    print("Analysing user graph...")

    # Plotting degree distributions
    degree_dist = np.bincount(scaffold.degree())
    x = range(degree_dist.size)

    fig = plt.figure()
    fig.suptitle("Degree distribution")
    plt.plot(x, degree_dist, c="blue")
    plt.xlabel("Number of connections")
    plt.ylabel("Number of nodes")
    plt.xscale("log")
    plt.yscale("log")

    # plt.show()
    fig.savefig(SAVE_PATH + f"mysql_{user}_dd.png")
    plt.close(fig)

    # Creating edge weight distribution
    edge_weights = scaffold.es['weight']
    counts = np.bincount(edge_weights)
    x = range(counts.size)

    fig, ax = plt.subplots()
    ax.plot(x, counts, 'bo')
    ax.set_xlabel("Weights (Number of uses)")
    ax.set_ylabel("Occurrences (Number of edges with particular weight)")
    ax.set_title("Edge weight distribution")
    plt.yscale("log")
    plt.xscale("log")
    plt.grid()
    fig.savefig(SAVE_PATH + f"mysql_{user}_ew.png")
    # plt.show()
    plt.close(fig)

def extract_scaffold(user_graph, user):
    """
    Extract scaffold from user graph.
    """
    print("Extract scaffold ...")

    # Creating subgraph by betweenness centrality
    propScaf = user_graph.es["weight"]
    ntile = np.percentile(propScaf, 97)
    sub_es = user_graph.es.select([v for v, b in enumerate(propScaf) if b >= ntile])
    sub_graph = user_graph.subgraph_edges(sub_es)
    scaffold = sub_graph.clusters().giant()
    return scaffold

def plot_scaffold(scaffold, user):
    """
    Plot scaffold.
    """

    # Plotting subgraph
    # Coloring edges
    colors = ["orange", "darkorange", "red", "blue"]
    for e in scaffold.es:
        weight = e['weight']
        if weight >= 15:
            e['color'] = colors[3]
        elif 8 <= weight < 15:
            e['color'] = colors[2]
        elif 3 <= weight < 8:
            e['color'] = colors[1]
        else:
            e['color'] = colors[0]

    # Clipping edge widths
    edge_widths = np.clip(a=scaffold.es['weight'], a_min=4, a_max=15)
    node_weights = scaffold.vs["weight"]
    maxw = max(node_weights)
    node_weights = np.divide(node_weights, maxw/100)
    # Styling graph
    visual_style = {"bbox": (3000, 3000), "margin": 17,
                    "vertex_color": 'grey',
                    "vertex_size": node_weights,
                    "vertex_label_size": 35,
                    "vertex_label": scaffold.vs["name"], "edge_curved": True,
                    "edge_width": edge_widths}

    # Set the layout
    try:
        layout = scaffold.layout("fr")
        visual_style["layout"] = layout
        save_name = f'mysql_{user}_reduced.png'
        igraph.plot(scaffold, SAVE_PATH + save_name, **visual_style)
        print(f"Graph from {user} analysed and plotted to {save_name}")
    except MemoryError:
        print(f"Memory error. Skipping to plot {user}'s graph.")

        

def load_graph(filename):
    """Loads graph from file"""
    return igraph.load(filename)


def save_graph(graph):
    """Saves scaffold graph in GML format"""
    igraph.save(graph, filename=LOAD_PATH + f'mysql_{USER}.gml')

def basic_stats(users):
    """Plots some basic statistics based on the user scaffolds"""
    vcounts = list()
    ecounts = list()
    avgDists = list()
    avgDeg = list()
    for index, user in enumerate(users):
        print(SAVE_PATH + f'mysql_{user}.gml')
        user_graph = load_graph(LOAD_PATH + f'mysql_{user}.gml')
        scaffold=extract_scaffold(user_graph, user)
        vcounts.append(scaffold.vcount())
        ecounts.append(scaffold.ecount())
        avgDeg.append(2*scaffold.ecount()/scaffold.vcount())
        avgDists.append(np.mean(scaffold.shortest_paths()))

    f, (ax1, ax2, ax3) = plt.subplots(3)
    ax1.plot(vcounts)
    ax1.plot(ecounts)
    ax1.set_title('Vertex and edge counts')
    ax2.plot(avgDists)
    ax2.set_title('Average distance')
    ax3.plot(avgDeg)
    ax3.set_title('Average degree')
    plt.show()

def stats_on_unions(users):
    """Plots some basic statistics based on the union of user scaffolds"""
    vcounts = list()
    ecounts = list()
    avgDists = list()
    for index, user in enumerate(users):
        print(SAVE_PATH + f'mysql_{user}.gml')
        user_graph = load_graph(LOAD_PATH + f'mysql_{user}.gml')
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
        user_graph = load_graph(LOAD_PATH + f'mysql_{user}.gml')
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
                user_graph1 = load_graph(LOAD_PATH + f'mysql_{user1}.gml')
                user_graph2 = load_graph(LOAD_PATH + f'mysql_{user2}.gml')
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
            user = line[:-1]
            all_users.append(user)

    # Load and analyse single scaffold
    #user = all_users[1]
    #user_graph = load_graph(LOAD_PATH + f'mysql_{user}.gml')
    #scaffold=extract_scaffold(user_graph, user)
    #plot_scaffold(scaffold, user)
    #plot_scaffold_distributions(scaffold, user)

    # Load and analyse all user scaffolds
    basic_stats(all_users)
    
if (__name__ == '__main__'):
    main()
