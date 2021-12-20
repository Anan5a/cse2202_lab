n = int(input("Enter the number of nodes: "))
e = int(input("Enter the number of edges: "))

adj_list = [[] for j in range(n)]

print("Enter edges in separate lines.")
for i in range(e):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)  # only when undirected

for line in adj_list:
    print("Adjacency list of vertex %d: " % adj_list.index(line), end='')
    for element in line:
        print(element, end=" ")
    print()


'''
Following code is to be independent
'''

n = int(input("Enter the number of nodes: "))
e = int(input("Enter the number of edges: "))

adj_list = {}

print("Enter edges in separate lines.")
for i in range(e):
    u, v = map(int, input("Enter %d: " % (i + 1)).split())
    adj_list[u].append(v)
    adj_list[v].append(u)  # only when undirected

print(adj_list)
