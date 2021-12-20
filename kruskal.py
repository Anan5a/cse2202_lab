def make_set(x, parent: dict, rank: dict):
    parent[x] = x
    rank[x] = 0


def find_set(x, parent: dict):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x], parent)
    return parent[x]


def union(x, y, rank: dict, parent: dict):
    px = find_set(x, parent)
    py = find_set(y, parent)
    if rank[px] < rank[py]:
        parent[px] = py
    elif rank[px] > rank[py]:
        parent[py] = px
    else:
        parent[py] = px
        rank[py] += 1


def kruskal(nodes: list, edges: list):
    parent = {}
    rank = {}
    selected = []
    weight = 0
    for node in nodes:
        make_set(node, parent, rank)
    sorted_edges = sorted(edges, key=lambda x: x[2])
    for edge in sorted_edges:
        if find_set(edge[0], parent) != find_set(edge[1], parent):
            selected.append(edge)
            union(edge[0], edge[1], rank, parent)
            weight += edge[2]
    return {'selected': selected, 'weight': weight}


def run_kruskal():
    nodes = input('Enter node names: ').split()
    edge_count = int(input('Enter number of edges: '))
    edges = []
    print('Enter Edges: ')
    for i in range(edge_count):
        u, v, w = input('Enter Edge (%d)' % (i + 1)).split(' ')
        edges.append([u, v, int(w)])
    result = kruskal(nodes, edges)
    print('Following edges produces MST')
    for item in result['selected']:
        print(item)
    print('Weight = %d' % result['weight'])
