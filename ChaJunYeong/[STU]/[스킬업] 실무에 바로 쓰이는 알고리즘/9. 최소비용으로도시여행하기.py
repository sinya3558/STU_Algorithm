import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
m = int(input())

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

s, e= map(int, input().split())

import heapq
def dijkstra(graph, start, end):
    dists = {node: 1e9 for node in graph}
    dists[start] = 0

    priority_q = [(0, start)]
    while priority_q:
        cur_dist, cur_node = heapq.heappop(priority_q)
        if cur_dist > dists[cur_node]:
            continue

        for next_node, weight in graph[cur_node]:
            dist = cur_dist + weight
            if dist < dists[next_node]:
                dists[next_node] = dist
                heapq.heappush(priority_q, (dist, next_node))

    return dists[end]

print(dijkstra(graph, s, e))