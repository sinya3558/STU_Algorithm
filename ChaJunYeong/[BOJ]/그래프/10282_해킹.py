import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    다익스트라 알고리즘으로 문제 해결
"""

def test_case(graph, start):
    import heapq

    # 다익스트라 알고리즘으로 신뢰하는 컴퓨터 감염시키기
    distances = [float('inf')] * (len(graph.keys()) + 1)
    distances[start] = 0

    q = [(0, start)]
    while q:
        cur_dist, cur_node = heapq.heappop(q)

        # 이미 감염되었다면 pass
        if cur_dist > distances[cur_node]:
            continue

        # 인접 컴퓨터 감염시키기
        for next_node, next_dist in graph[cur_node].items():
            new_dist = cur_dist + next_dist
            if new_dist < distances[next_node]:
                distances[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))

    # 감염시키는데 가장 오래 걸리는 컴퓨터 찾기기
    max_time = -1
    for time in distances[1:]:
        if time != float('inf') and max_time < time:
            max_time = time
    return [len(distances) - distances.count(float('inf')), max_time]


T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    graph = {i:{} for i in range(1, n + 1)}
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b][a] = s
    print(*test_case(graph, c))
