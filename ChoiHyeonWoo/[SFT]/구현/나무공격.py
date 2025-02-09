n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
L1, R1 = map(int, input().split())
L2, R2 = map(int, input().split())
L1 -= 1
R1 -= 1
L2 -= 1
R2 -= 1
for i in range(L1, L1 + 5):
    for j in range(m):
        if board[i][j] == 1:
            board[i][j] = 0
            break

for i in range(L2, L2 + 5):
    for j in range(m):
        if board[i][j] == 1:
            board[i][j] = 0
            break

cnt = 0
for i in range(n):
    cnt += sum(board[i])

print(cnt)