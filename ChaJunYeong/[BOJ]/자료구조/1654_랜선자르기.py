import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    알고리즘 분류 힌트보고 해결결
"""

k, n = map(int, input().split())
k_ropes = [int(input()) for _ in range(k)]

# 이분 탐색으로 접근
# 최소 길이 1cm, 최대 길이 maximum rope 길이

# 1. mid 기준으로 줄 잘라서 만들 수 있는 줄 갯수 세기
# 2. 만들 수 있는 줄 갯수가 적으면, 더 작게 잘라야함 (r = mid - 1)
# 3. 만들 수 있는 줄 갯수가 많으면, 더 길게 잘라볼 수 있음 (l = mid + 1)
# 4. 이때, mid 값이 현재 기준 최댓값이면 저장

l, r = 1, max(k_ropes)
result = 0
while l <= r:
    mid = (l + r) // 2

    cnt = 0 # 1
    for rope in k_ropes:
        cnt += (rope // mid)

    if cnt < n: # 2
        r = mid - 1

    elif n <= cnt: # 3
        if result < mid: result = mid # 4
        l = mid + 1

print(result)