import sys
def input():
    return sys.stdin.readline().rstrip()
 
arr = [list(map(int, input().split())) for _ in range(19)]

# 00:27:28 + 00:39:26
# 1. 좌상단부터 확인
# 2. 백돌 / 흑돌이 놓여져 있으면
#   2-1. 가로 확인
#   2-2. 세로 확인
#   2-3. 대각선 2방향 확인

"""
    대각선 방향을 ↘ ↙ 가 아니라 ↘ ↗ 로 확인했어야 함...
"""

def check_omok(y, x, dy, dx):

    for i in range(1, 5):
        # 범위를 벗어나지 않으면서, 기존 돌과 같은 색이면 +1
        ny, nx = y + dy * i, x + dx * i
        if not (0 <= ny < 19 and 0 <= nx < 19 and arr[y][x] == arr[ny][nx]):
            return False
    
        # 오목을 달성한 상태에서 육목인지 확인
        # 1. 반대 방향쪽 육목
        # 2. 같은 방향쪽 육목
        if i == 4:
            ny, nx = y + dy * 5, x + dx * 5
            if 0 <= ny < 19 and 0 <= nx < 19 and arr[y][x] == arr[ny][nx]:
                return False
            
            ny, nx = y + dy * (-1), x + dx * (-1)
            if 0 <= ny < 19 and 0 <= nx < 19 and arr[y][x] == arr[ny][nx]:
                return False
    return True


for y in range(19):
    for x in range(19):
        if arr[y][x] == 0:
            continue

        for dy, dx in ((0, 1), (1, 0), (1, 1), (-1, 1)):
            if check_omok(y, x, dy, dx):
                print(arr[y][x])
                print(y+1, x+1)
                exit()

print(0)