import sys
board = [list(map(int, input().split())) for _ in range(3)]
check = []
for i in range(3):
    if board[i][0] == board[i][1] == board[i][2]:
        print(0)
        sys.exit()
    elif board[i][0] != board[i][1] and board[i][1] != board[i][2] and board[i][0] != board[i][2]:
        check.append(2)
    else:
        if 0 < abs(board[i][0] - board[i][1]):
            check.append(abs(board[i][0] - board[i][1]))
        elif 0 < abs(board[i][1] - board[i][2]):
            check.append(abs(board[i][1] - board[i][2]))
        elif 0 < abs(board[i][0] - board[i][2]):
            check.append(abs(board[i][0] - board[i][2]))

for i in range(3):
    field = []
    for j in range(3):
        field.append(board[j][i])
    if field[0] == field[1] == field[2]:
        print(0)
        sys.exit()
    elif field[0] != field[1] and field[1] != field[2] and field[0] != field[2]:
        check.append(2)
    else:
        if 0 < abs(field[0] - field[1]):
            check.append(abs(field[0] - field[1]))
        elif 0 < abs(field[1] - field[2]):
            check.append(abs(field[1] - field[2]))
        elif 0 < abs(field[0] - field[2]):
            check.append(abs(field[0] - field[2]))

print(abs(min(check)))