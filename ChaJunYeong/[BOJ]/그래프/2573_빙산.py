import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    구현, 시뮬레이션 문제처럼 해결
    전체 구성 자체는 어렵지 않음
    빙산이 두 덩어리인지 체크할 경우, BFS/DFS 탐색 필요

    0. 우선 전체 빙산에 대한 정보 저장

    1. 1년 뒤 빙산 상태 업데이트
    2. 빙산에 대한 정보 업데이트
    3-1. 빙산이 없으면 0 출력
    3-2. 빙산이 두 덩어리면 현재 시간 출력 → BFS
    3-3. 빙산이 두 덩어리가 아니면 1부터 반복

"""

# import sys
# sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def check_sea(y, x):
    num_sea = 0
    for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        if arr[y + dy][x + dx] <= 0:
            num_sea += 1
    return num_sea


from collections import deque
def check_ice_two(info_ice):
    q = deque()
    isVisited = [[False] * m for _ in range(n)]
    cnt = 0

    for (iy, ix), _ in info_ice:
        if isVisited[iy][ix]:
            continue

        cnt += 1
        q.append((iy, ix))
        isVisited[iy][ix] = True
        while q:
            cy, cx = q.popleft()
            for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                ny, nx = cy + dy, cx + dx
                if arr[ny][nx] > 0 and not isVisited[ny][nx]:
                    q.append((ny, nx))
                    isVisited[ny][nx] = True

    return True if cnt >= 2 else False


# 0. 빙산의 초기 정보 저장
ice = list()
for i in range(1, n-1):
    for j in range(1, m-1):
        if arr[i][j] != 0:
            ice.append(((i, j), check_sea(i, j)))

time = 0
while True:    
    # 1. 1년 뒤 빙산 녹기 (주의! 다 녹은 다음에 정보가 업데이트 되어야 함함)
    time += 1
    for (iy, ix), num_sea in ice:
        arr[iy][ix] -= num_sea
        if arr[iy][ix] <= 0:
            arr[iy][ix] = 0

    # 2. 업데이트 된 빙산의 정보 저장
    new_ice = list()
    for (iy, ix), num_sea in ice:
        if 0 < arr[iy][ix]:
            new_ice.append(((iy, ix), check_sea(iy, ix)))
    ice = new_ice[:]

    # 3-1. 빙산이 다 녹았으면 0 출력
    if len(ice) == 0:
        print(0)
        break
    
    # 3-2. 빙산이 다 녹지 않았으면 두 덩어리인지 체크
    elif check_ice_two(ice):
        print(time)
        break
