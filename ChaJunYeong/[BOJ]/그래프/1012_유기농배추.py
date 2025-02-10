import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    1. 유기농 배추가 있는 곳에 배추흰지렁이 풀어놓기
    2. BFS 탐색을 통해 연결된 배추 찾아 모두 방문
    3. 이미 방문한 배추는 다시 방문하지 않기
"""

def test_case(arr):
    n = len(arr)
    m = len(arr[0])
    isVisited = [[False] * m for _ in range(n)]

    from collections import deque
    def _bfs(y, x):
        q = deque()
        q.append((y, x))
        isVisited[y][x] = True

        while q:
            y, x = q.popleft()
            for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == 1 and not isVisited[ny][nx]:
                    q.append((ny, nx))
                    isVisited[ny][nx] = True
        return 

    cnt = 0
    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1 and not isVisited[y][x]:
                _bfs(y, x)
                cnt += 1
    return cnt


T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for _ in range(k):
        u, v = map(int, input().split())
        arr[v][u] = 1
    print(test_case(arr))