import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [input() for _ in range(n)]

# 1. 정사각형 좌상단부터 차례대로 돌기 (0, n-8) (0, m-8) 까지 가능
# 2. 좌상단이 B일 경우 바꿔야 하는 체스판 색
# 3. 좌상단이 W일 경우 바꿔야 하는 체스판 색
# 4. 최솟값 구하기

result = sys.maxsize

def cnt_recolor_board_white(y, x):
    cnt = 0
    for iy in range(8):
        for ix in range(8):
            if   (iy + ix) % 2 == 0 and arr[y + iy][x + ix] == 'B':
                cnt += 1
            elif (iy + ix) % 2 == 1 and arr[y + iy][x + ix] == 'W':
                cnt += 1
    return cnt

def cnt_recolor_board_black(y, x):
    cnt = 0
    for iy in range(8):
        for ix in range(8):
            if   (iy + ix) % 2 == 0 and arr[y + iy][x + ix] == 'W':
                cnt += 1
            elif (iy + ix) % 2 == 1 and arr[y + iy][x + ix] == 'B':
                cnt += 1
    return cnt

for y in range(n-8 + 1):
    for x in range(m-8 + 1):
        result = min(result, cnt_recolor_board_black(y, x), cnt_recolor_board_white(y, x))

print(result)