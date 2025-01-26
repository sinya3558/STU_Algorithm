from collections import deque
import sys
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    global date
    Q = deque()
    Q.append
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                Q.append((i,j))
    while Q:
        temp = Q.popleft()
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 1
                Q.append((nx, ny))
                date[nx][ny] = date[temp[0]][temp[1]] + 1


maximum = -25434
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
date = [[0] * M for _ in range(N)]
bfs()
for i in range(N):
    for j in range(M):
        maximum = max(maximum, date[i][j])
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            print(-1)
            sys.exit(0)
print(maximum)