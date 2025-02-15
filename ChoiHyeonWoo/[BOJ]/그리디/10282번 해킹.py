import sys
import heapq
input = sys.stdin.readline
T = int(input())
ans = []
for test_case in range(T):
    n, d, c = map(int, input().split())
    INF = 999999999999999999
    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    def dijkstra(start):
        distance[start] = 0
        q = []
        heapq.heappush(q, (0, start))
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = i[1] + dist
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost, i[0]))
    dijkstra(c)
    virus = 0
    answer = 0
    for x in range(len(distance)):
        if distance[x] == INF:
            distance[x] = 0
        else:
            virus+=1
    answer = max(distance)
    ans.append((virus, answer))
for virus, answer in ans:
    print(virus, answer)