import sys
def input():
    return sys.stdin.readline().rstrip()


"""
    00:20:07.78

    방향 그래프에서, 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램 작성

    풀이:
        다익스트라 알고리즘 사용
        주의 해야 하는 것 : 현재 노드에서 다른 노드로 이동할 때 간선이 여러 개 존재할 수 있음

        * 다익스트라 알고리즘에서 우선순위큐를 사용하는 이유
            큐에서, 같은 노드를 방문하는 경우가 발생할 수 있음
            이때, 해당 노드에 방문하는 거리가 짧은 방법 먼저 사용한다면,
            방문하는 거리가 긴 방법은 pass 함으로써 시간을 절약할 수 있음 (불필요한 방문 pass)
"""


# 그래프 정보 저장
V, E = map(int, input().split())
K = int(input())
graph = {i: [] for i in range(1, V + 1)}
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

# 다익스트라 알고리즘 구현
import heapq

# 각 노드까지 최단 거리 저장
distances = [float('inf')] * (V+ 1)
distances[K] = 0

# 시작점에서 출발
q = [(0, K)]
while q:
    cur_dist, cur_node = heapq.heappop(q)

    # 해당 루트로 오는 거리가 더 길다면 pass
    if distances[cur_node] < cur_dist: continue

    # 그렇지 않으면 인접한 노드로 이동해보기
    for nxt_node, nxt_dist in graph[cur_node]:
        new_dist = cur_dist + nxt_dist

        # 만약 인접한 노드로 최단 거리만큼 이동할 수 있다면 queue에 넣기
        if new_dist < distances[nxt_node]:
            distances[nxt_node] = new_dist
            heapq.heappush(q, (new_dist, nxt_node))

for i in range(1, V + 1):
    if distances[i] == float('inf'): print("INF")
    else: print(distances[i])