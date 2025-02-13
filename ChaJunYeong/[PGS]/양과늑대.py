from collections import deque

# BFS Solution
def bfs_solution(info, edges):
    graph = {node:[] for node in range(len(info))}
    for parent, child in edges:
        graph[parent].append(child)

    q = deque()
    max_lamb = 0
    
    """
        사실상 완전 탐색에 가까움
        현재 노드로부터 탐색 가능한 노드들을 돌며, 탐색 가능한 노드의 경우 queue에 넣기
            - 해당 노드를 방문했을 때, 늑대 < 양 이어야 함
                - 그렇지 않을 경우 pass
                - 조건을 만족하는 경우
                    - 이후 방문 가능한 자식 노드를 추가하여 queue에 넣기
    """
    
    # node, lamb, wolf, 탐색 가능한 노드 리스트
    q.append((0, 1, 0, set(graph[0])))
    while q:
        cur_node, lamb, wolf, available = q.popleft()
        max_lamb = max(max_lamb, lamb)

        for next_node in available:
            new_lamb = lamb + (info[next_node] == 0)
            new_wolf = wolf + (info[next_node] == 1)

            if new_lamb <= new_wolf:
                continue

            new_available = available.copy()
            new_available.remove(next_node)
            new_available.update(graph[next_node])

            q.append((next_node, new_lamb, new_wolf, new_available))

    return max_lamb


# DFS Solution
def dfs_solution(info, edges):
    graph = {node:[] for node in range(len(info))}
    for parent, child in edges:
        graph[parent].append(child)

    """
        깊이 우선 탐색도 마찬가지 방식으로 접근하면 될 듯
        현재 탐색 가능한 노드들 중 앞에 있는 것부터 우선적으로 계속 방문
            - 이때, lamb <= wolf 이면 빠져나오기
            - 만약 계속 탐색이 가능하다면
                - 현재 노드를 제거한 뒤, 방문 가능한 노드에 자식 노드들을 추가로 넣기
    """

    def dfs(node, lamb, wolf, available):
        nonlocal max_lamb

        lamb += (info[node] == 0)
        wolf += (info[node] == 1)

        if lamb <= wolf:
            return
        
        max_lamb = max(max_lamb, lamb)
        for next_node in available:
            new_available = available.copy()
            new_available.remove(next_node)
            new_available.update(graph[next_node])
            dfs(next_node, lamb, wolf, new_available)

    max_lamb = 0
    dfs(0, 0, 0, set(graph[0]))
    return max_lamb     



# 1 Test Case
print(
    dfs_solution(
        [0,0,1,1,1,0,1,0,1,0,1,1], 
        [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
    )
)

# 2 Test Case
print(
    dfs_solution(
        [0,1,0,1,1,0,1,0,0,1,0],
        [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
    )
)