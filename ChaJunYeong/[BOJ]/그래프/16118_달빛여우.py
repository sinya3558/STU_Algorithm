import sys
def input():
    return sys.stdin.readline().rstrip()


# 입력 받기
N, M = map(int, input().split())
graph = {i:[] for i in range(1, N + 1)}
for _ in range(M):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))


import heapq
"""
    달빛 여우 최단 거리 구하기
    일정한 속도로 달리는 달빛 여우의 최단 거리는 다익스트라 알고리즘으로 구현할 수 있음
"""
def fox():
    distances = [float('inf')] * (N+1)
    distances[1] = 0

    q = [(0, 1)]
    while q:
        cur_dist, cur_node = heapq.heappop(q)

        # 만약 현재 노드로 오는 더 짧은 방법이 있다면 pass
        if distances[cur_node] < cur_dist:
            continue

        # 현재 방법이 최선이라면, 인접한 다음 노드로 이동
        for nxt_node, nxt_dist in graph[cur_node]:
            new_dist = cur_dist + nxt_dist
            if new_dist < distances[nxt_node]:
                distances[nxt_node] = new_dist
                heapq.heappush(q, (new_dist, nxt_node))
                
    return distances[1:]


"""
    달빛 늑대 최단 거리 구하기
    똑같이 다익스트라로 구현하지만 달빛 여우와는 다르게 구현되어야 함
    
    고려할 점.
    1. 달빛 늑대는 2배 빠르게 / 2배 느리게 상태를 반복함
    2. 이 덕분에, 한 바퀴를 돌아서 가는 경우가 최적인 상태가 될 때도 있음

    1에 의해, 각 상태 별로 해당 노드에 도달하는 최적의 거리를 저장해야 함
    2에 의해, 1번 노드로 되돌아올 수 있다는 점을 고려하여, 1번의 최단 거리를 0으로 초기화 하면 안됨
"""
def wolf():
    distances = [[float('inf')] * (N+1) for _ in range(2)]

    # 거리, 노드, 0 == 달리는 상태, 1 == 쉬어야 하는 상태
    q = [(0, 1, 0)] 
    while q:
        cur_dist, cur_node, rest = heapq.heappop(q)

        # 현재 상태에서 현재 노드로 오는 더 짧은 방법이 있다면 pass
        if distances[rest][cur_node] < cur_dist:
            continue

        # 현재 상태에서 현재 방법이 최선이라면, 인접한 다음 노드로 이동
        for nxt_node, nxt_dist in graph[cur_node]:
            new_dist = cur_dist + nxt_dist * (0.5 if rest == 0 else 2)
            if new_dist < distances[(rest + 1) % 2][nxt_node]:
                distances[(rest + 1) % 2][nxt_node] = new_dist
                heapq.heappush(q, (new_dist, nxt_node, (rest + 1) % 2))

    return [0 if i == 1 else min(distances[0][i], distances[1][i]) for i in range(1, N + 1)]

cnt = 0
fox_cost = fox()
wolf_cost = wolf()
print(fox_cost)
print(wolf_cost)
for i in range(N):
    if fox_cost[i] < wolf_cost[i]:
        cnt += 1
print(cnt)