import sys
def input():
    return sys.stdin.readline().rstrip()

# import sys
# sys.stdin = open('./input.txt', 'r')

# Input
n = int(input())
arr = [input() for _ in range(n)]
isVisited = [[False] * n for _ in range(n)]

# 연결된 단지 탐색
# 4 방향 탐색
#   1. 움직인 곳이 범위 밖인 경우, 탐색 안함
#   2. 움직인 곳이 단지가 아닌 경우, 탐색 안함
#   3. 그 외의 경우는 탐색 후보
from collections import deque
def bfs(y, x):
    q = deque()
    q.append((y, x))
    isVisited[y][x] = True
    cnt = 1

    # 탐색 시작
    while q:
        y, x = q.popleft()
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0<=ny<n and 0<=nx<n and arr[ny][nx] == '1' and not isVisited[ny][nx]:
                q.append((ny, nx))
                isVisited[ny][nx] = True
                cnt += 1
    return cnt

# 전체 단지를 돌면서, 집인 곳부터 연결된 곳을 탐색
cnt = list()
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1' and not isVisited[i][j]:
            cnt.append(bfs(i, j))

# Output
print(len(cnt))
for item in sorted(cnt):
    print(item)
