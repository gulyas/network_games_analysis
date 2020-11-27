import igraph


def getId(state):
    cellId = 0
    exponent = 15
    for row in state:
        for column in row:
            if column == 1:
                cellId += pow(2, exponent)
            exponent -= 1
    return cellId


def getState(cellId):
    state = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    binary = '{0:09b}'.format(cellId)
    index = 0
    for char in binary:
        state[index // 4][index % 4] = int(char)
        index += 1
    return state


def invert(state, row, col):
    if state[row][col] == 1:
        state[row][col] = 0
    else:
        state[row][col] = 1
    return

def main():
    # ---- MAIN PART ----
    graph = igraph.Graph(65536)

    for i in range(65536):
        print(i)
        state1 = getState(i)
        # neighbours with inverting rows
        for j in range(4):
            state2 = state1
            for k in range(4):
                invert(state2, j, k)
            neighbourId = getId(state2)
            graph.add_edge(i, neighbourId)

        # neighbours with inverting columns
        for j in range(4):
            state2 = state1
            for k in range(4):
                invert(state2, k, j)
            neighbourId = getId(state2)
            graph.add_edge(i, neighbourId)

        # neighbours with inverting diagonals
        state2 = state1
        for j in range(4):
            invert(state2, j, j)
        neighbourId = getId(state2)
        graph.add_edge(i, neighbourId)

        state2 = state1
        for j in range(4):
            invert(state2, 3 - j, j)
        neighbourId = getId(state2)
        graph.add_edge(i, neighbourId)

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
