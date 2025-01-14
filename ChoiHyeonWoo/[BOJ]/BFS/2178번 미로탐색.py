from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
dis = [[0] * M for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
Q = deque()
board[0][0] = 0
Q.append((0,0))
while Q:
    temp = Q.popleft()
    for i in range(4):
        nx = temp[0] + dx[i]
        ny = temp[1] + dy[i]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:
            dis[nx][ny] = dis[temp[0]][temp[1]] + 1
            Q.append((nx,ny))
            board[nx][ny] = 0
print(dis[N-1][M-1] + 1)