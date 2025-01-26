import sys
def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
isVisited = [0] * (10 ** 6)

# -- 문제 풀이 --
# 1. 현재 위치에서 갈 수 있는 위치 넣기 n-1, n+1, 2n
#   조건 1. 이때, 범위 내여야 함
#   조건 2. 이때, 한 번도 방문한 적 없어야 함
#   1-1. 현재 위치보다 1초 증가, 앞으로 방문할 포인트 큐에 넣기
# 2. 현재 위치가 k 위치이면 종료

# -- 회고 --
# 접근은 좋았으나, 구현상 실패 문제가 있었음
# 문제를 읽고, 짧게 고민한 다음 바로 코딩에 들어가서 그런 것 같음
# 손코딩으로 어느정도 틀 만들어 놓은 후 코딩에 들어갈 것

from collections import deque
cur_points = deque()
cur_points.append(n)

while cur_points:
    cur_p = cur_points.popleft()

    if cur_p == k:
        break

    for next_p in (cur_p - 1, cur_p + 1, 2 * cur_p):
        if 0 <= next_p <= 200001 and isVisited[next_p] == 0:
            isVisited[next_p] = isVisited[cur_p] + 1
            cur_points.append(next_p)

print(isVisited[k])