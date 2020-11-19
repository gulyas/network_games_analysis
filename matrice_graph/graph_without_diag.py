import igraph

SAVE_PATH = "D:\\network_games\\matrice"


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


def rotate(state, id, isRow):
    rowOrCol = [0, 0, 0]
    temp = 0
    if isRow:
        rowOrCol = state[id]
        temp = rowOrCol[0]
        for i in range(2):
            rowOrCol[i] = rowOrCol[i + 1]
        rowOrCol[2] = temp
        state[id] = rowOrCol
    else:
        for i in range(3):
            rowOrCol[i] = state[i][id]
        temp = rowOrCol[0]
        for j in range(2):
            rowOrCol[j] = rowOrCol[j + 1]
        rowOrCol[2] = temp
        for k in range(3):
            state[k][id] = rowOrCol[k]
    return


def main():
    # ---- MAIN PART ----
    graph = igraph.Graph(512)

    for i in range(512):
        state = getState(i)
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

        # azok a szomszédok, akiket rotációval kapni
        # sorok rotációja
        for j in range(3):
            state = getState(i)
            rotate(state, j, True)
            neighbourId = getId(state)
            graph.add_edge(i, neighbourId)
        # oszlopok rotációja
        for j in range(3):
            state = getState(i)
            rotate(state, j, False)
            neighbourId = getId(state)
            graph.add_edge(i, neighbourId)

    # többszörös élek törlése
    graph.simplify(multiple=True)
    graph.vs["label"] = range(graph.vcount())

    components = graph.components()
    component_sizes = components.sizes()

    print(component_sizes)
    # print(components.giant())

    diam = igraph.Graph.diameter(graph, False, False, None)
    apl = igraph.Graph.average_path_length(graph, False, False)
    cl = igraph.Graph.transitivity_undirected(graph)
    print(graph.summary())
    print(graph.vcount(), graph.ecount())
    print("diameter: ", diam, " path length: ", apl, " clustering: ", cl)
    # print(graph.degree())
    print("average degree: ", igraph.mean(graph.degree()))

    # for component in components:
    #    print(component)

    layout = graph.layout("lgl")
    visual_style = {"vertex_size": 40, "edge_width": 2, "layout": layout, "bbox": (3000, 3000)}

    # igraph.plot(graph, SAVE_PATH + "graphall.eps", **visual_style)

    # Save graph
    # graph.save(SAVE_PATH + "matrice_graph.gml")


if __name__ == '__main__':
    main()
