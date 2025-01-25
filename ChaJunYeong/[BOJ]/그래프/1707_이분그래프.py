import sys
def input():
    return sys.stdin.readline().rstrip()

# 코드 참고 : https://ji-gwang.tistory.com/293

""" 1/2/3차 시도
    메모리 초과
        → 그래프를 2차원 배열로 표현해서 그런 것 같음
        → graph를 인접한 노드들로만 채우는 방법으로 바꿈

    arr = [[0] * v for _ in range(v)]
        for _ in range(e):
            x, y = map(int, input().split())
            arr[x-1][y-1] = 1
            arr[y-1][x-1] = 1
        isVisited = [0] * v
"""


from collections import deque
k = int(input())

def bfs(start, group):
    q = deque([start])
    isVisited[start] = group

    while q:
        cur_v = q.popleft()

        # 현재 접점으로부터 인접한 노드 방문
        #   1. 아직 방문하지 않는 노드라면
        #       이때, 인접한 노드는 현재 노드랑 다른 그룹에 속해야 함
        #   2. 방문했던 노드인데, 현재 노드와 같은 그룹에 속해있다면
        #       break

        for i in graph[cur_v]:   
            if not isVisited[i]:
                q.append(i)
                isVisited[i] = isVisited[cur_v] * (-1)  
            elif isVisited[i] == isVisited[cur_v]:      
                return False
            
    return True


for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]  # 빈 그래프 생성
    isVisited = [False] * (v + 1)       # 방문 접점 그래프 생성

    for _ in range(e):  # 그래프에 인접한 접점만 넣기
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, v + 1):
        if not isVisited[i]:
            result = bfs(i, 1)
            if not result:
                break

    print("YES" if result else "NO")
