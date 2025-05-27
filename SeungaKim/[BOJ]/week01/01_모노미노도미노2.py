# https://www.acmicpc.net/problem/20061
# 1:10
'''
아...이거 테트리스?
빨간색 맵에 블럭 쌓고, 동시에 파랑 & 초록으로 이동 -> 맵의 끝에 다다르거나 다른 블럭에 닿으면 멈춤
    블루는 -> y axis fixing
    green -> x axis

그 다음 블럭또 빨간색 맵을 기준으로 두고 파랑과 초록으로 이동 -> 쌓임
    blue -> delete one colum if itfs filled (+ 1 pt) -> left moves to Right
    green -> del a row (+ 1pt)-> left moves to Bottom

light zone
    light blue (col 0 & 1) -> del the last 1 or 2 cols ->  move to R --> no point 
    light green (row 0 & 1) -> del the last 1 or 2 rows -> move to B

행이나 열이 타일로 가득찬 경우(1)와 연한 칸에 블록이 있는 경우(2)가 동시에 발생할 수 있다.
이 경우에는 행이나 열이 타일로 가득 찬 경우가 없을 때까지 점수를 획득하는 과정이 모두 진행된 후, 연한 칸에 블록이 있는 경우를 처리해야 한다.

    -> points (priority) -> move to B or R (Q.이거 그냥 두고 처리하는듯) -> count secrete zone -> move 22

블록은 보드에 놓인 이후에 다른 블록과 합쳐지지 않는다. 
블록을 놓은 위치가 순서대로 주어졌을 때, 
얻은 점수와 초록색 보드와 파란색 보드에 타일이 있는 칸의 개수를 모두 구해보자
'''
# 1: 38
'''
입력
첫째 줄에 블록을 놓은 횟수 N(1 ≤ N ≤ 10,000)이 주어진다.

둘째 줄부터 N개의 줄에 블록을 놓은 정보가 한 줄에 하나씩 순서대로 주어지며, t x y와 같은 형태이다.

t = 1: 크기가 1×1인 블록을 (x, y)에 놓은 경우
t = 2: 크기가 1×2인 블록을 (x, y), (x, y+1)에 놓은 경우
t = 3: 크기가 2×1인 블록을 (x, y), (x+1, y)에 놓은 경우
블록이 차지하는 칸이 빨간색 칸의 경계를 넘어가는 경우는 입력으로 주어지지 않는다.

출력
첫째 줄에 블록을 모두 놓았을 때 얻은 점수를 출력한다.

둘째 줄에는 파란색 보드와 초록색 보드에서 타일이 들어있는 칸의 개수를 출력한다.
'''
import sys

N = int(input())

if not 1 <= N <= 10000:
    sys.exit()

# R 4x4 / B (4x4) + 4x6 / G (4x4) + 6x4
# B : 4 x 10 (point cols) -> 시작점 (-, 4) ~ (-, 9)
# G : 10 x 4 (point rows) ->       (4, -) ~ (9, -)
b_rows, b_cols = 4, 10
g_rows, g_cols = 10, 4
blue_2d = [[0] * b_cols for i in range(b_rows)]
green_2d = [[0] * g_cols for i in range(g_rows)]

# getting user inputs
for _ in range(N):
    block_info = sys.stdin.readline()
    t, x, y = map(int, block_info.split())
    if not 1 <= t <= 3 or not 0 <= x <= 3 or not 0 <= y <= 3:
        print("invalid input value.")
        break
    
    # CASE 1:  1x1
    if t == 1:
        # BLUE, blue_2d[x][y] = 1
        ''' 아아아아아 멍청이 -= 1 안된다고오오
        for idx in range(4, 10):    # idx: 4 ~ 9
            if blue_2d[x][idx] == 1:
                # if its filled
                idx -= 1
                blue_2d[x][idx] = 1
            else:   
                # not filled
                blue_2d[x][idx] = 1
        '''
        idx_col = 0
        while idx_col < 10 and blue_2d[x][idx_col] == 0:    # 비어있을 경우!
            idx_col += 1                                    # 오른쪽으로 붙어
        idx_col -= 1                                        # 길막힘 당했으면, 뒤로 백
        blue_2d[x][idx_col] = 1                             # 채워넣어

        # GREEN
        idx_row = 0
        while idx_row < 10 and green_2d[idx_row][y] == 0:
            idx_row += 1
        green_2d[idx_row - 1][y] = 1
        
    # CASE 2: 1X2
    elif t == 2:
        # blue_2d[x][y] = 1
        # blue_2d[x][y+1] = 1
        # BLUE, 얘를 계속 반복해야하나 func 써서 줄일방법 어디없나...!
        col = 0
        while col < 9 and blue_2d[x][col] == 0 and blue_2d[x][col+1] == 0:
            col += 1
        col -= 1
        blue_2d[x][col] = 1
        blue_2d[x][col+1] = 1

        # GREEN
        row = 0
        while row < 10 and green_2d[row][y] == 0 and green_2d[row][y + 1] == 0:
            row += 1
        row -= 1
        green_2d[row][y] = 1
        green_2d[row][y + 1] = 1


    
    # CASE 3 : 2X1
    elif t == 3:
        # blue_2d[x][y] = 1
        # blue_2d[x+1][y] = 1
        # BLUE
        col = 0
        while col < 10 and blue_2d[x][col] == 0 and blue_2d[x + 1][col] == 0:
            col += 1
        col -= 1
        blue_2d[x][col] = 1
        blue_2d[x + 1][col] = 1

        # GREEN
        row = 0
        while row < 9 and green_2d[row][y] == 0 and green_2d[row + 1][y] == 0:
            row += 1
        row -= 1
        green_2d[row][y] = 1
        green_2d[row + 1][y] = 1
    
    else:
