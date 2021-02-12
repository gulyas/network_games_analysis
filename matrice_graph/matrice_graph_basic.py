"""
The basic Matrice graph.
Board size: 3x3
Transformations: inversion
Directions: horizontal, vertical, diagonal
"""
import igraph


def get_id(state):
    """
    Assigns a unique natural number to each board state.
    :param state: Two dimensional array containing the state of the game board
    :return: Id number of the state
    """
    cell_id = 0
    exponent = 8
    for row in state:
        for column in row:
            if column == 1:
                cell_id += pow(2, exponent)
            exponent -= 1
    return cell_id


def get_state(cell_id):
    """
    Gets the state from a state identification number.
    :param cell_id: Natural number identifying the state
    :return: Two dimensional array containing the state
    """
    state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    binary = '{0:09b}'.format(cell_id)
    index = 0
    for char in binary:
        state[index // 3][index % 3] = int(char)
        index += 1
    return state


def invert(state, row, col):
    """
    Inversion on a state cell
    :param state: Two dimensional array containing the state
    :param row: Row index of the cell
    :param col: Column index of the cell
    :return: Nothing
    """
    if state[row][col] == 1:
        state[row][col] = 0
    else:
        state[row][col] = 1
    return


def main():
    # ---- MAIN PART ----
    # Undirected graph, because the only transformation applied in this variant is reversible.
    graph = igraph.Graph(512)

    for i in range(512):
        # neighbours with inverting rows
        for j in range(3):
            state = get_state(i)
            for k in range(3):
                invert(state, j, k)
            neighbour_id = get_id(state)
            graph.add_edge(i, neighbour_id)

        # neighbours with inverting columns
        for j in range(3):
            state = get_state(i)
            for k in range(3):
                invert(state, k, j)
            neighbour_id = get_id(state)
            graph.add_edge(i, neighbour_id)

        # neighbours with inverting diagonals
        state = get_state(i)
        for j in range(3):
            invert(state, j, j)
        neighbour_id = get_id(state)
        graph.add_edge(i, neighbour_id)

        state = get_state(i)
        for j in range(3):
            invert(state, 2 - j, j)
        neighbour_id = get_id(state)
        graph.add_edge(i, neighbour_id)

    # deleting multiple edges
    graph.simplify(True, True)
    graph.vs["label"] = range(graph.vcount())

    # Check whether graph is fully connected
    components = graph.components()
    component_sizes = components.sizes()

    print(component_sizes)
    # print(components.giant())

    # Print statistics
    diam = igraph.Graph.diameter(graph, False, False, None)
    apl = igraph.Graph.average_path_length(graph, False, False)
    cl = igraph.Graph.transitivity_undirected(graph)
    print("diameter: ", diam, " path length: ", apl, " clustering: ", cl)

    for component in components:
        print(component)

    print(graph.neighbors(0))

    # Plot graph
    layout = graph.layout("kk")
    igraph.plot(graph, "graph.pdf", layout=layout)


if __name__ == '__main__':
    main()
