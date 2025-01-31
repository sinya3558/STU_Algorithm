import sys
def input():
    return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
isVisited = [[False] * m for _ in range(n)]


from collections import deque
q = deque()
q.append((0, 0, 1))
isVisited[0][0] = True

while q:
    y, x, length = q.popleft()

    # 목표지점 도달
    if y == n-1 and x == m-1:
        break
    
    for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        ny, nx = y + dy, x + dx

        # 1. 미로 안이어야 함
        # 2. 다시 방문하지 않아야 함
        # 3. 경로여야 함
        if 0 <= ny < n and 0 <= nx < m and not isVisited[ny][nx] and arr[ny][nx] == '1':
            q.append((ny, nx, length + 1))

print(length)
