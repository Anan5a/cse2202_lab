from math import inf
from queue import PriorityQueue


class Node:
    def __init__(self, node):
        self.name = node
        self.d = inf
        self.parent = None
        self.isVisited = False
        self.adj = []

    def __lt__(self, other):
        return self.d < other.d


def dijkstra(nodes: dict, source: str):
    q = PriorityQueue()
    nodes[source].d = 0
    nodes[source].parent = source
    q.put(nodes[source])

    while not q.empty():
        u = q.get()
        u.isVisited = True
        for v in u.adj:
            vn, w = v[0], v[1]
            if nodes[vn].isVisited is False and nodes[vn].d > u.d + w:
                nodes[vn].d = u.d + w
                nodes[vn].parent = u.name
                q.put(nodes[vn])


def print_path(nodes: dict, dest):
    if nodes[dest].parent != dest:
        print_path(nodes, nodes[dest].parent)
    print(dest, end=' ')


def run_dijkstra():
    vertex = input("Enter the vertex list: ").split(' ')
    edges = int(input("Enter number of edges: "))

    nodes = {}

    for v in vertex:
        nodes[v] = Node(v)
    for e in range(edges):
        u, v, w = input("Enter edge %d info: " % (e + 1)).split(' ')
        nodes[u].adj.append([v, int(w)])
    source = input("Source vertex = ")

    # nodes[source].d = 0
    # nodes[source].parent = source

    dijkstra(nodes, source)
    print("Name Key/Weight Parent")

    for node in nodes:
        print("Vertex name: %s, Cost: %d, Path:" % (node, nodes[node].d), end=' ')
        print_path(nodes, node)
        print()
