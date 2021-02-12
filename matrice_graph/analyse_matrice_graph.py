"""
Analysing the graph behind the Matrice android game.
"""
import igraph
import matplotlib.pyplot as plt
import numpy as np

GRAPH_FILE = "..\\matrice_graph\\matrice_graph.gml"
SAVE_PATH = "D:\\network_games\\matrice\\"


def load_graph(filename):
    """Loads graph from a file"""
    return igraph.load(filename=filename)


def plot_graph_stats(graph):
    """Plot statistics of the Matrice and a BA graph in order to facilitate comparison.
    Uses:
        -- matplotlib
        -- numpy
        -- igraph
    """

    # Creating a BA graph as a basis for comparison
    ba_graph = igraph.Graph.Barabasi(n=512, directed=True)

    # Plotting mean degrees and standard deviation
    degrees = graph.degree()
    avg = np.mean(degrees)
    stdev = np.std(degrees)
    closeness = graph.closeness()

    ba_degrees = ba_graph.degree()
    ba_avg = np.mean(ba_degrees)
    ba_stdev = np.std(ba_degrees)
    ba_closeness = ba_graph.closeness()

    fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2)
    fig.suptitle("Mean degree and standard deviation")
    ax0.errorbar(1, avg, yerr=stdev, fmt='-o', elinewidth=2, capsize=4)
    ax0.set_title('Matrice graph')
    ax0.set_ylabel('Degree')
    ax0.axes.get_xaxis().set_visible(False)
    ax0.set_ylim(11, 19)

    ax1.errorbar(1, ba_avg, yerr=ba_stdev, fmt='-o', elinewidth=2, capsize=4, c='green')
    ax1.set_title('BA scale-free graph')
    ax1.axes.get_xaxis().set_visible(False)
    ax1.set_ylim(-2, 6)

    plt.show()
    # fig.savefig(SAVE_PATH + f'degree_mean_std.png')
    # fig.close()

    # Plotting degree distributions
    degree_dist = np.bincount(degrees)
    x = range(degree_dist.size)
    ba_degree_dist = np.bincount(ba_graph.degree())
    ba_x = range(ba_degree_dist.size)

    fig = plt.figure()
    fig.suptitle("Degree distributions")
    plt.plot(x, degree_dist, c="blue", label="Matrice")
    plt.plot(ba_x, ba_degree_dist, c="green", label="BA")
    plt.xlabel("Number of connections")
    plt.ylabel("Number of nodes")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()

    plt.show()
    # fig.savefig(SAVE_PATH + f'degree_dist.png')
    # fig.close()

    # Plotting closeness centrality
    y = np.random.rand(len(closeness))
    ba_y = np.random.rand(len(ba_closeness))

    fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharex='row')
    fig.suptitle("Closeness centrality")
    ax0.scatter(closeness, y, alpha=0.8, c='blue')
    ax1.scatter(ba_closeness, ba_y, alpha=0.8, c='green')

    ax0.set_title("Matrice graph")
    ax0.set_xlabel("Closeness")
    ax0.axes.get_yaxis().set_visible(False)
    ax1.set_title('BA scale-free graph')
    ax1.set_xlabel("Closeness")
    ax1.axes.get_yaxis().set_visible(False)

    ax0.grid(True)
    ax1.grid(True)
    fig.tight_layout()

    plt.show()
    fig.savefig(SAVE_PATH + f'closeness_centrality.png')
    # fig.close()


def main():
    graph = load_graph(GRAPH_FILE)
    plot_graph_stats(graph)


if __name__ == '__main__':
    main()