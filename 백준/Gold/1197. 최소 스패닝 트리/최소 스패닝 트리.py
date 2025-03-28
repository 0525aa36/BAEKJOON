import sys
sys.setrecursionlimit(10**6)

V, E = map(int, sys.stdin.readline().split())
edges = []

for _ in range(E):
    edges.append(list(map(int, sys.stdin.readline().split())))

# Union-Find 초기화
root = dict()
for i in range(1, V+1):
    root[i] = i

def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]

def union(x, y):
    x = find(x)
    y = find(y)
    root[y] = x

edges = sorted(edges, key=lambda x: x[2])
total_cost = 0

for edge in edges:
    if find(edge[0]) == find(edge[1]):
        continue
    else:
        total_cost += edge[2]
        union(edge[0], edge[1])

print(total_cost)
