from collections import deque
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
n, m = map(int, input().split())
board = []
store_xy = []
start_xy = []
a = 0
cnt = 0
for _ in range(n):
    board.append(list(map(int, input().split())))
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    store_xy.append((x,y))
    a += 10
    board[x][y] = a

def isFinish():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == -1:
                cnt+=1
            if cnt == m:
                return True
    return False

def goBaseCamp(cnt):
    Q = deque()
    visited = [[0] * n for _ in range(n)]
    base_camp_list = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == cnt * 10:
                Q.append((i,j))
                visited[i][j] == 1
    while Q:
        temp = Q.popleft()
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if board[nx][ny] == 0 or board[nx][ny] == 1 or board[nx][ny] >= 10:
                    visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                    Q.append((nx, ny))
                    if board[nx][ny] == 1:
                        #base_camp_list에는 베이스 캠프의 좌표와 편의점으로부터의 거리가 기록 돼있다.
                        base_camp_list.append((nx, ny, visited[nx][ny]))
    base_camp_list = sorted(base_camp_list, key = lambda x: (x[2], x[0],x[1]))
    board[base_camp_list[0][0]][base_camp_list[0][1]] = 2
    return base_camp_list[0][0], base_camp_list[0][1]

def move_one(x, y, num):
    come = [[None] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    Q = deque()
    Q.append((x,y))
    store_x = store_xy[num][0]
    store_y = store_xy[num][1]
    while Q:
        temp = Q.popleft()
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if board[nx][ny] == 0 or board[nx][ny] >= 10 or board[nx][ny] == 1:
                    Q.append((nx, ny))
                    visited[nx][ny] = 1
                    come[nx][ny] = (temp[0], temp[1])
    for i in range(n):
        for j in range(n):
            if come[i][j] == None:
                come[i][j] = (0,0)
    xx, yy = store_x, store_y
    while 1:
        if come[xx][yy] == (x, y):
            return xx, yy
        else:
            xx, yy = come[xx][yy]

while 1:
    if isFinish() == True:
        break
    cnt += 1
    if start_xy:
        for i in range(0, len(start_xy)):
            if board[store_xy[i][0]][store_xy[i][1]] == -1:
                continue
            next_x, next_y = move_one(start_xy[i][0], start_xy[i][1], i)
            start_xy[i] = (next_x, next_y)
            if store_xy[i][0] == start_xy[i][0] and store_xy[i][1] == start_xy[i][1]:
                board[store_xy[i][0]][store_xy[i][1]] = -1
    if cnt <= m:
        x, y  = goBaseCamp(cnt)
        start_xy.append((x,y))
    # print(cnt)
    # print(start_xy)
    # for x in board:
    #     print(x, end = ' ')
    #     print()
    # print()
print(cnt)