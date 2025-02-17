import heapq

def dijkstra(graph, start):
    # 1. 거리 테이블 초기화
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    # 2. 우선순위 큐 (힙) 초기화: (거리, 노드)
    priority_queue = [(0, start)]

    while priority_queue:
        # 3. 현재까지의 최단 거리가 가장 짧은 노드 꺼내기
        current_dist, current_node = heapq.heappop(priority_queue)

        # 4. 이미 처리된 노드라면 무시
        if current_dist > distance[current_node]:
            continue

        # 5. 인접한 노드 확인
        for neighbor, weight in graph[current_node]:
            new_dist = current_dist + weight

            # 6. 더 짧은 경로 발견 시 거리 갱신
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(priority_queue, (new_dist, neighbor))

    return distance

# 예제 그래프 (인접 리스트)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('C', 1), ('D', 5)],
    'C': [('D', 2)],
    'D': [],
    'E': [('A', 1)]
}

# 다익스트라 알고리즘 실행
start_node = 'A'
result = dijkstra(graph, start_node)

# 결과 출력
for node in sorted(result):
    print(f"최단 거리: {start_node} → {node} = {result[node]}")
