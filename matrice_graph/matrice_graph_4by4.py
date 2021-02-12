"""
Variant of the Matrice graph.
The game with a boardsize of 4 by 4.
"""
import igraph


def get_id(state):
    """
    Assigns a unique natural number to each board state.
    :param state: Two dimensional array containing the state of the game board
    :return: Id number of the state
    """
    cell_id = 0
    exponent = 15
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
    state = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    binary = '{0:09b}'.format(cell_id)
    index = 0
    for char in binary:
        state[index // 4][index % 4] = int(char)
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
    graph = igraph.Graph(65536)

    for i in range(65536):
        print(i)
        state1 = get_state(i)
        # neighbours with inverting rows
        for j in range(4):
            state2 = state1
            for k in range(4):
                invert(state2, j, k)
            neighbour_id = get_id(state2)
            graph.add_edge(i, neighbour_id)

        # neighbours with inverting columns
        for j in range(4):
            state2 = state1
            for k in range(4):
                invert(state2, k, j)
            neighbour_id = get_id(state2)
            graph.add_edge(i, neighbour_id)

        # neighbours with inverting diagonals
        state2 = state1
        for j in range(4):
            invert(state2, j, j)
        neighbour_id = get_id(state2)
        graph.add_edge(i, neighbour_id)

        state2 = state1
        for j in range(4):
            invert(state2, 3 - j, j)
        neighbour_id = get_id(state2)
        graph.add_edge(i, neighbour_id)

    # deleting multiple edges
    graph.simplify(True, True)
    graph.vs["label"] = range(graph.vcount())

    components = graph.components()
    component_sizes = components.sizes()

    print(component_sizes)
    # print(components.giant())

    for component in components:
        print(component)


if __name__ == '__main__':
    main()
