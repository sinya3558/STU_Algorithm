'''
보시는 분 계신지 모르겠지만 첫 번째 #으로 주석해둔 코드는 DFS로 
풀려다가 실패 한 것입니다~~
재귀함수 호출이 너무 많아서 오류 나네요 임의로 깊이 더 늘봤는데 메모리 초과
떴습니다.
'''

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# test_board = [[0] * M for _ in range(N)]

# def wind(air_con, x, y, d, visited, test_cnt):
#     test_board[x][y] = 1
#     visited[x][y] = 1
#     nx, ny = x + dx[d], y + dy[d]
#     if nx < 0 or nx >= N or ny < 0 or ny >= M or (nx, ny) == air_con or test_cnt >= 3:
#         return
#     if visited[nx][ny] == 1:
#         test_cnt += 1
#     else:
#         test_cnt = 0
#     if board[nx][ny] == 1:
#         if d == 2:
#             # d = 3
#             test_board[nx][ny] = 1
#             return
#         elif d == 3:
#             # d = 2
#             test_board[nx][ny] = 1
#             return
#     elif board[nx][ny] == 2:
#         if d == 0:
#             # d = 1
#             test_board[nx][ny] = 1
#             return
#         elif d == 1:
#             # d = 0
#             test_board[nx][ny] = 1
#             return
#     elif board[nx][ny] == 3:
#         if d == 0:
#             d = 3
#         elif d == 1:
#             d = 2
#         elif d == 2:
#             d = 1
#         else:
#             d = 0
#     elif board[nx][ny] == 4:
#         d = (d + 2 + 4) % 4
#     wind(air_con, nx, ny, d, visited, test_cnt)
#     return

# def dir(x, y):
#     for d in range(4):
#         air_con = (x, y)
#         visited = [[0] * M for _ in range(N)]
#         test_cnt = 0
#         wind(air_con, x, y, d, visited, test_cnt)

# for i in range(N):
#     for j in range(M):
#         if board[i][j] == 9:
#             dir(i, j)

# cnt = 0
# for i in range(N):
#     cnt += sum(test_board[i])
# print(cnt)



'''
그래서 BFS로 풀었습니다.
board : 자리, 에어컨, 물건이 있는 격자.
check_board : 민상이가 앉을 수 있는 자리를 1로 둔 격자(기본은 0).
visited : 방문처리. 3차원 리스트로 만들었고, 만약 같은 방향으로 방문 처리 된다면 
더이상 진행하지 않도록 했습니다. --> 같은 방향이 있다면 이미 처리했기 때문이죠.
해당 방문처리 안해서 시간초과 떴었네요.
cnt : 민상이가 앉을 수 있는 자리의 수. 즉, 정답.
'''

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
check_board = [[0] * M for _ in range(N)]
visited = [[[] for _ in range(M)] for _ in range(N)]
def wind(x, y):
    check_board[x][y] = 1
    for d in range(4):
        Q = deque()
        visited[x][y].append(d)
        Q.append((x, y))
        while Q:
            temp = Q.popleft()
            nx = temp[0] + dx[d]
            ny = temp[1] + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if (nx, ny) == (x, y) or board[nx][ny] == 9:
                    break
                if visited[nx][ny] and visited[nx][ny][-1] == d:
                    break
                visited[nx][ny].append(d)
                check_board[nx][ny] = 1
                Q.append((nx, ny))
                if board[nx][ny] == 1:
                    if d == 2 or d == 3:
                        check_board[nx][ny] = 1
                        break
                    elif d == 3:
                        check_board[nx][ny] = 1
                        break
                elif board[nx][ny] == 2:
                    if d == 0:
                        check_board[nx][ny] = 1
                        break
                    elif d == 1:
                        check_board[nx][ny] = 1
                        break
                elif board[nx][ny] == 3:
                    if d == 0:
                        d = 3
                    elif d == 1:
                        d = 2
                    elif d == 2:
                        d = 1
                    else:
                        d = 0
                elif board[nx][ny] == 4:
                    d = (d + 2 + 4) % 4

for i in range(N):
    for j in range(M):
        if board[i][j] == 9:
            wind(i, j)

cnt = 0
for i in range(N):
    cnt += sum(check_board[i])
print(cnt)