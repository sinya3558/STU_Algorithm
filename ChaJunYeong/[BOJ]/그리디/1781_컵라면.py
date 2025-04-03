import sys
def input():
    return sys.stdin.readline().rstrip()

# 입력 받기
N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[0], -x[1]))

"""
    우선순위 힙으로 문제 해결.

    1. 데드라인 순으로, 가장 많은 포인트를 받을 수 있는 과제 순으로 정렬
    2. 시간 내로 문제를 해결할 수 있는 과제부터 해결
    3. 이때, 더 많은 포인트를 얻을 수 있다면, 가장 적은 포인트를 받는 문제 대신 해결

    ex) 
    (1, 1), (2, 7), (2, 6)의 경우,
    처음에는 (1, 1), (2, 7)의 문제를 해결하지만
    (1, 1) 대신 (2, 6)의 문제를 해결하는 것이 더 많은 포인트를 얻을 수 있기 때문에
    (2, 6), (2, 7) 순으로 문제 해결
"""

import heapq
ans = []
for deadline, point in arr:

    if len(ans) < deadline:
        heapq.heappush(ans, point)

    elif len(ans) == deadline and ans[0] < point:
        heapq.heappop(ans)
        heapq.heappush(ans, point)

print(sum(ans))
