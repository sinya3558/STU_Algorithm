import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    2차원 배열 Deep Copy : 
        next_arr = [a[:] for a in arr]
"""

# 체스판 크기 결정
n = int(input())
board = [[0] * n for _ in range(n)]


def remove_row(arr, row):
    for i in range(n):
        if arr[row][i] == 0: arr[row][i] = 2
    return arr

def remove_column(arr, col):
    for i in range(n):
        if arr[i][col] == 0: arr[i][col] = 2
    return arr

def remove_diagonal(arr, row, col):
    l, r = col, col
    for i in range(row + 1, n):
        l, r = l - 1, r + 1
        if 0 <= l < n and arr[i][l] == 0: arr[i][l] = 2
        if 0 <= r < n and arr[i][r] == 0: arr[i][r] = 2
    return arr

def valid_board(arr, row, col):
    arr = remove_row(arr, row)
    arr = remove_column(arr, col)
    arr = remove_diagonal(arr, row, col)
    return arr


# 체스판 위에 Queen 놓기
result = 0
def queens(arr, row):
    global result

    # 마지막 줄(Depth - 1 == n)에 도달했으면, 빈 자리 (0)의 갯수만큼 Queen을 놓을 수 있음
    if row == n - 1:
        result += arr[n - 1].count(0)
        return

    else:
    # 마지막 줄이 아니면
    # 1. 해당 줄(Depth)에 Queen을 놓을 빈 자리 (0)가 없으면 break
        if arr[row].count(0) == 0: 
            return

    # 2. Queen을 놓을 수 있으면
        # 2-1. Queen을 놓고
        # 2-2. 가로 줄 제거
        # 2-3. 세로 줄 제거
        # 2-4. 대각선 제거
        for col in range(n):
            if arr[row][col] == 0:
                next_arr = [a[:] for a in arr]
                next_arr[row][col] = 1
                next_arr = valid_board(next_arr, row, col)
                queens(next_arr, row + 1)

queens(board, 0)
print(result)
