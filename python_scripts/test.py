from igraph import Graph, plot

SAVE_PATH = "D:\\network_games\\"


def plot_er():
    """Plots a visualization of an E-R random graph"""
    g = Graph.Erdos_Renyi(n=100, m=100)
    visual_style = {"bbox": (3000, 3000), "margin": 100, "vertex_color": 'orange', "vertex_size": 50,
                    "vertex_label_size": 10, "edge_curved": False, "edge_color": 'black', "edge_width": 7}
    layout = g.layout("fr")
    visual_style["layout"] = layout
    save_name = f'er_layout.png'
    plot(g, SAVE_PATH + save_name, **visual_style)


def plot_ba():
    """Plots a visualization of an B-A scale-free graph"""
    g = Graph.Barabasi(n=150)
    visual_style = {"bbox": (3000, 3000), "margin": 100, "vertex_color": 'blue', "vertex_size": 50,
                    "vertex_label_size": 10, "edge_curved": False, "edge_color": 'black', "edge_width": 7}
    layout = g.layout("fr")
    visual_style["layout"] = layout
    save_name = f'ba_layout.png'
    plot(g, SAVE_PATH + save_name, **visual_style)


def main():
    g = Graph().K_Regular(20, 3)
    # for edge in g.es:
    #    print(edge)
    # plot_er()
    # plot_ba()


if __name__ == '__main__':
    main()
