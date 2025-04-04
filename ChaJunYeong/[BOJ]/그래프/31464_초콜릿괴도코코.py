import sys
def input():
    return sys.stdin.readline().rstrip()


N = int(input())
arr = [list(input()) for _ in range(N)]

"""
    단위 초콜릿을 끊어 냈을 때 모든 초콜릿이 하나의 그래프로 연결되어 있어야 함.
    이때, 해당 그래프에서 임의의 인접한 노드의 간선을 끊어냈을 때, 두 "그래프(트리)"로 나뉘는 조건.
"""

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 2단계 조건을 만족하는지 확인.
from collections import deque
def check_condition(y, x):
    new_arr = [row[:] for row in arr]
    new_arr[y][x] = '.'

    # 1. 남아있는 초콜릿이 있는지 확인
    pieces = [(i, j) for i in range(N) for j in range(N) if new_arr[i][j] == '#']

    # 1-1. 남아있는 초콜릿이 없으면 False
    if len(pieces) == 0:
        return False
    

    # 2. BFS로 모든 초콜릿이 하나로 연결되어 있는지 확인
    start = pieces[0]
    visited = [[False] * N for _ in range(N)]

    q = deque([start])
    visited[start[0]][start[1]] = True
    connected_cnt = 1
    while q:
        cy, cx = q.popleft()
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < N:                        # 초콜릿 내부에 있으면서
                if not visited[ny][nx] and new_arr[ny][nx] == '#': # 방문하지 않은 초콜릿인 경우
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    connected_cnt += 1
    
    # 2-1. 만약 연결되어 있지 않다면 pass (연결된 초콜릿의 개수가 남아있는 초콜릿 개수와 다를 경우)
    if connected_cnt != len(pieces):
        return False

    """
        3. 남아 있는 초콜릿 중 어떤 연결을 끊어도 2개의 조각이 나오도록 만들려면, 
        남은 초콜릿이 연결 그래프로 볼 때 트리 구조여야 함.
        (트리는 연결 그래프이면서, 임의의 간선을 제거했을 때 2개의 조각으로 나뉠 수 있기 때문)
    """

    # 3. 트리의 조건: 그래프의 간선의 수 = 노드의 수 - 1
    # 격자이므로 오른쪽과 아래쪽만 체크 (간선 중복 방지)
    edge_cnt = 0
    for cy in range(N):
        for cx in range(N):
            if new_arr[cy][cx] == '#':
                for dy, dx in [(1, 0), (0, 1)]:
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < N and 0 <= nx < N and new_arr[ny][nx] == '#':
                        edge_cnt += 1
    return edge_cnt == len(pieces) - 1



# 주어진 초콜릿을 하나씩 끊어냈을 때 조건을 만족하는지 확인.
result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '#':
            if check_condition(i, j):
                result.append((i + 1, j + 1))

print(len(result))
for y, x in result:
    print(y, x)