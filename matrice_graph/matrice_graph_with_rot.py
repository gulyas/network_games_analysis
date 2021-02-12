"""
Variant of the Matrice graph.
Board size: 3x3
Transformations: inversion, rotation
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


def rotate(state, n, is_row):
    """
    Rotation of a row or column of the state
    :param state: Two dimensional array containing the state
    :param n: Number of the row or column
    :param is_row: Indicates whether to rotate a row or a column
    :return: Nothing
    """
    row_or_col = [0, 0, 0]
    if is_row:
        row_or_col = state[n]
        temp = row_or_col[0]
        for i in range(2):
            row_or_col[i] = row_or_col[i + 1]
        row_or_col[2] = temp
        state[n] = row_or_col
    else:
        for i in range(3):
            row_or_col[i] = state[i][n]
        temp = row_or_col[0]
        for j in range(2):
            row_or_col[j] = row_or_col[j + 1]
        row_or_col[2] = temp
        for k in range(3):
            state[k][n] = row_or_col[k]
    return


def main():
    # ---- MAIN PART ----
    # Directed graph, because the rotation transformation applied here is irreversible.
    graph = igraph.Graph(512, directed=True)

    for i in range(512):
        state = get_state(i)
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

        # neighbours with rotating
        # rows
        for j in range(3):
            state = get_state(i)
            rotate(state, j, True)
            neighbour_id = get_id(state)
            graph.add_edge(i, neighbour_id)
        # or columns
        for j in range(3):
            state = get_state(i)
            rotate(state, j, False)
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
    print(graph.summary())
    print(graph.vcount(), graph.ecount())
    print("diameter: ", diam, " path length: ", apl, " clustering: ", cl)
    # print(graph.degree())
    print("average degree: ", igraph.mean(graph.degree()))

    for component in components:
        print(component)

    # Plot graph
    layout = graph.layout("kk")
    visual_style = {"vertex_size": 40, "edge_width": 2, "layout": layout, "bbox": (4000, 4000)}

    igraph.plot(graph, "graphall.pdf", **visual_style)


if __name__ == '__main__':
    main()
