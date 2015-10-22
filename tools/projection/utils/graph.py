import conll
import numpy as np
from collections import defaultdict


class Edge:
    """TODO.
    """
    def __init__(self, source, target, label, weight):
        self.source = int(source)
        self.target = int(target)
        self.label = label
        self.weight = weight

class Graph:
    """TODO.
    """
    nodes = defaultdict(conll.ConllToken)

    def __init__(self):
        self.nodes[0] = conll.ConllToken.null_token()  # graph root (wall node)
        self.matrix = np.zeros(shape=(5, 5))

    # def __init__(self, tp_graph):
    #    """TODO: reads a TurboParser structure into the numpy matrix.
    #    """
    #    return

    def add_node(self, conll_token):
        self.nodes[conll_token.idx] = conll_token

    def add_edge(self, edge):
        self.matrix[edge.source][edge.target] = edge.weight

e = Edge(2, 3, "none", 0.01)
g = Graph()
g.add_edge(e)

print(g.matrix)
