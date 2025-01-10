# import sys
# sys.stdin = open('input.txt', 'r')

import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    1번째 시도에서 시간초과 → 1, 2 물건을 만났을 때 종료?
    2번째 시도 시간초과 → sum 함수 문제?
    3번째 시도 시간초과 → input 함수 선언
    4번째 시도 시간초과 → 또 다른 air condition을 만났을 때 종료
    pypy로 하니 통과;
"""

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 에어컨 자리 찾기
air_pos = list()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 9:
            air_pos.append((i, j))

# 물건에 따른 방향 전환
def change_dir(x, direction):
    if x == 1:
        if direction[1] != 0:
            direction = [0, 0]
    elif x == 2:
        if direction[0] != 0:
            direction = [0, 0]
    elif x == 3:
        direction = [-direction[1], -direction[0]]
    elif x == 4:
        direction = [direction[1], direction[0]]
    return direction


# 에어컨으로부터 시작
can_sit = [[0] * m for _ in range(n)]
for ay, ax in air_pos:
    can_sit[ay][ax] = 1

    # 4 방향 순서대로 돌기
    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]: 
        y, x = ay, ax

        while True:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < m) or arr[ny][nx] == 9:
                break

            y, x = ny, nx
            can_sit[y][x] = 1
            dy, dx = change_dir(arr[y][x], [dy, dx])

            if (dy, dx) == (0, 0):
                break

count = 0
for i in range(n):
    count += can_sit[i].count(1)
print(count)
