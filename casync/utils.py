from six import print_


def print_graph(n, depth=0, fprint=print_):
    fprint(' '*2*depth, n.id, type(n).__name__)
    for c in n.children:
        print_graph(c, depth+1)
