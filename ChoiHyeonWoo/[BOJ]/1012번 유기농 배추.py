from collections import deque
T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = []
for _ in range(T):
    cnt1 = 0
    M ,N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    for i in range(K):
        a, b = map(int, input().split())
        board[b][a] = 1
    Q = deque()
    for j in range(N):
        for k in range(M):
            if board[j][k] == 1:
                cnt1 += 1
                Q.append((j,k))
                board[j][k] = 0
                while Q:
                    temp = Q.popleft()
                    for i in range(4):
                        nx = temp[0] + dx[i]
                        ny = temp[1] + dy[i]
                        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:
                            board[nx][ny] = 0
                            Q.append((nx, ny))
    cnt.append(cnt1)
for x in cnt:
    print(x)