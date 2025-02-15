import sys
input = sys.stdin.readline
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    edges = []
    add = 0
    parent = [0] * m
    for i in range(m):
        parent[i] = i
    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((x, y, z))
        add += z

    edges.sort(key = lambda x : x[2])
    result = 0
    for edge in edges:
        a, b, cost = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    print(add - result)