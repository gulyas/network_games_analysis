"""
Assembles graph of all Wikipedia links in the English Wikipedia.
"""
import csv
import igraph

PATH = "D:\\network_games\\"
FILENAME = "wikilink_graph.2018-03-01.csv"
EXPORT_FILE = "wikilink_graph"


def read_graph(filename):
    """Reads and assembles graph from a tab delimited CSV file"""

    with open(filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter='\t')
        print("Parsed file: {}".format(filename))

        graph = igraph.Graph()
        line_count = 0
        vertex_count = 0
        for row in csv_reader:
            # Ignoring first row with column names
            if line_count == 0:
                print(f'Columns: {", ".join(row)}')
                line_count += 1
            else:
                line_count += 1
                source = row[1]
                target = row[3]
                # Inserting source and target nodes of the link if they are absent
                try:
                    graph.vs.find(source)
                except ValueError:
                    graph.add_vertex(name=source)
                    vertex_count += 1
                    print("Vertices added: {}".format(vertex_count))
                try:
                    graph.vs.find(target)
                except ValueError:
                    graph.add_vertex(name=target)
                    vertex_count += 1
                graph.add_edge(source=source, target=target)
        return graph


def export_graph(graph, filename):
    """Saves graph in GML format"""
    print("Exporting...")
    igraph.write(graph, filename, format="graphmlz")
    print("Exported file to {}".format(filename))


def main():
    # try:
    graph = read_graph(PATH + FILENAME)
    export_graph(graph, PATH + EXPORT_FILE)
    # except Exception as error:
    #   print(error)


if __name__ == '__main__':
    main()
