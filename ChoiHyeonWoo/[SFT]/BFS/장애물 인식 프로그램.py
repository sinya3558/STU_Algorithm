from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
board = [list(map(int, input())) for _ in range(N)]
cnt = 0
visited = [[0] * N for _ in range(N)]
answer = []
def find_block(x, y):
    global cnt
    Q = deque()
    Q.append((x, y))
    visited[x][y] = 1
    cnt += 1
    block_cnt = 1
    while Q:
        temp = Q.popleft()
        for k in range(4):
            nx = temp[0] + dx[k]
            ny = temp[1] + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and board[nx][ny] == 1:
                block_cnt += 1
                Q.append((nx, ny))
                visited[nx][ny] = 1
    answer.append(block_cnt)

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == 0:
            find_block(i, j)
print(cnt)
for x in answer:
    print(x)