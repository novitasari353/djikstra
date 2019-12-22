from collections import deque
from collections import namedtuple

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):

        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('edges data is wrong: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]




