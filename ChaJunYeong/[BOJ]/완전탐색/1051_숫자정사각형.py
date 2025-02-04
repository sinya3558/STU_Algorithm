import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

# 처음 생각
# 1. 좌상단 꼭짓점부터 하나씩 돌면서 정사각형인지 체크
#    이때, max 길이보다 작은 정사각형이라면 체크할 필요가 없음
#   1-1. 같은 행에 동일한 숫자가 있는지 체크
#   1-2. 1-1이 참이라면, 똑같은 길이의 열에 동일한 숫자가 있는지 체크
#   1-3. 1-2가 참이라면, 똑같은 길이의 행과 열에 동일한 숫자가 있는지 체크
#   1-4. 1-3이 참이라면, max값 체크

"""
    항상 범위 체크를 잘 해둘 것
    1. 좌상단 꼭짓점부터 하나씩 돌면서 정사각형인지 체크
    2. 같은 행에 동일한 숫자가 있음, 해당 숫자가 지금까지 찾은 가장 큰 정사각형보다 더 큰 곳에 위치
        2-1. 이 경우, 해당 index와 변의 길이를 저장
        2-2. 동일한 길이만큼 떨어진 열이 index를 넘어간다면 넘어가기
        2-3. index를 넘어가지 않는다면, 같은 열 + 같은 열/행에 동일한 숫자가 있는지 확인
        2-4. 1-3이 참이라면 가장 큰 정사각형의 변의 길이 업데이트트
"""

max_square = 0

# 1.
for y in range(n):
    for x in range(m):
        num = arr[y][x]

        for nx in range(x, m):
            # 2-1.
            if arr[y][nx] == num and max_square < (nx-x) + 1:
                ny = y + nx - x

                # 2-2.
                if n <= ny:
                    continue

                # 2-3. 2-4.
                if arr[ny][x] == num and arr[ny][nx] == num:
                    max_square = nx - x + 1

print(max_square ** 2)
