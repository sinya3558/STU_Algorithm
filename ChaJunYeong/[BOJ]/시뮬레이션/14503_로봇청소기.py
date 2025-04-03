import sys
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
cy, cx, cd = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

"""
    00:26:31.48
"""

# 북 동 남 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


# 청소기가 동작을 멈출 때 까지 계속 동작하기 
ans = 2
while True:

    # 1. 현재 칸이 청소되지 않았으면 청소
    if arr[cy][cx] == 0:
        arr[cy][cx] = ans
        ans += 1

    # 2. 주변 4칸 중 청소되지 않은 빈칸이 있으면
    # 2-1-1. 반시계 방향으로 회전 후, 청소되지 않은 빈칸이면 전진
    # 2-1-2. 반시계 방향으로 회전 후, 청소된 빈칸이면 다시 회전
    rotate_cnt = 1
    while rotate_cnt <= 4:
        nd = (cd - rotate_cnt) % 4
        ny, nx = cy + dy[nd], cx + dx[nd]
        if arr[ny][nx] == 0:
            cy, cx, cd = ny, nx, nd
            break
        rotate_cnt += 1

    # 3. 주변 4칸 중 청소되지 않은 빈칸이 없으면
    # 3-1. 후진
    # 3-2. 뒤쪽이 벽이면 작동 멈춤
    if rotate_cnt == 5:
        nd = (cd - 2) % 4
        ny, nx = cy + dy[nd], cx + dx[nd]
        if arr[ny][nx] != 1:
            cy, cx = ny, nx
        elif arr[ny][nx] == 1:
            print(ans - 2)
            break
