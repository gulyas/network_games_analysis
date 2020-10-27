import igraph


# mind az 512 állapothoz egyértelműen hozzárendel egy számot 0 és 511 között
def getId(state):
    cellId = 0
    exponent = 8
    for row in state:
        for column in row:
            if column == 1:
                cellId += pow(2, exponent)
            exponent -= 1
    return cellId


# az állapotot azonosító számból visszaszámolja az állapotot
def getState(cellId):
    state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    binary = '{0:09b}'.format(cellId)
    index = 0
    for char in binary:
        state[index // 3][index % 3] = int(char)
        index += 1
    return state


# inverzió egy mátrix mezőn
def invert(state, row, col):
    if state[row][col] == 1:
        state[row][col] = 0
    else:
        state[row][col] = 1
    return


def main():
    # ---- MAIN PART ----
    graph = igraph.Graph(512)

    for i in range(512):
        # azok a szomszédok, amiket sorok inverziójával kapni
        for j in range(3):
            state = getState(i)
            for k in range(3):
                invert(state, j, k)
            neighbourId = getId(state)
            graph.add_edge(i, neighbourId)

        # azok a szomszédok, amiket oszlopok inverziójával kapni
        for j in range(3):
            state = getState(i)
            for k in range(3):
                invert(state, k, j)
            neighbourId = getId(state)
            graph.add_edge(i, neighbourId)

        # azok a szomszédok, amiket átlók inverziójával kapni
        state = getState(i)
        for j in range(3):
            invert(state, j, j)
        neighbourId = getId(state)
        graph.add_edge(i, neighbourId)

        state = getState(i)
        for j in range(3):
            invert(state, 2 - j, j)
        neighbourId = getId(state)
        graph.add_edge(i, neighbourId)

    # többszörös élek törlése
    graph.simplify(True, True)
    graph.vs["label"] = range(graph.vcount())

    components = graph.components()
    component_sizes = components.sizes()

    print(component_sizes)
    # print(components.giant())

    diam = igraph.Graph.diameter(graph, False, False, None)
    apl = igraph.Graph.average_path_length(graph, False, False)
    cl = igraph.Graph.transitivity_undirected(graph)
    print("diameter: ", diam, " path length: ", apl, " clustering: ", cl)

    for component in components:
        print(component)

    print(graph.neighbors(0))

    layout = graph.layout("kk")
    igraph.plot(graph, "graph.pdf", layout=layout)


if __name__ == '__main__':
    main()
