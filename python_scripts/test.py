from igraph import Graph


def main():
    g = Graph().K_Regular(20,3)
    for edge in g.es:
        print(edge)


if __name__ == '__main__':
    main()
