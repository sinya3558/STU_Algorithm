import sys
def input():
    return sys.stdin.readline().rstrip()

# 입력 받기
N, C = map(int, input().split())
arr = list(map(int, input().split()))


"""
    N개의 물건을 가지고, 최대 C만큼의 무게를 넣을 수 있는 가방에 물건을 넣는 방법 찾기
    N = 2, C = 1이고, 주어진 물건의 무게가 각각 a=1, b=1 이라면
        1. a, b 둘 다 안 넣는 경우
        2. a 만 넣는 경우
        3. b 만 넣는 경우
    총 3가지 경우의 수가 있음
    결국 각 물건을 넣었을 때와 넣지 않았을 때의 경우의 수를 따지며 가방에 물건을 넣을 수 있는지 확인해야 함
    이때, N=30일 경우, 최악의 경우엔 1,073,741,824번 계산해야 하는 불상사가 발생할 수 있음


    # Meet in the Middle (MITM)
    따라서 가운데 인덱스를 기준으로 리스트를 두 개로 분리하여, 각 리스트 안에서의 조합의 경우의 수를 구해주기
    (이 경우, 최악의 경우에 2^30 만큼의 계산량을, 2 * 2^15로 크게 줄여줄 수 있다.)
    
    # 이분 탐색
    각 경우의 수의 합을 리스트 안에 담고 정렬한 다음, 이분탐색으로 경우의 수 찾기
    한쪽 리스트를 기준으로 물건 무게의 합을 돌면서, 다른 쪽 리스트에서 최대로 넣을 수 있는 무게의 합 index 찾기
    (이미 정렬되어 있기 때문에 최대 index만 찾아도 됨됨)
    
"""

# Meet in the Middle (MITM 알고리즘)
mid = N // 2
a, a_sum = arr[:mid], [0]
b, b_sum = arr[mid:], [0]

from itertools import combinations
for i in range(1, len(a) + 1):
    for sub in combinations(a, i):
        a_sum.append(sum(sub))

for i in range(1, len(b) + 1):
    for sub in combinations(b, i):
        b_sum.append(sum(sub))
b_sum.sort()

# 이분 탐색
ans = 0
for a_weight in a_sum:

    # 가방에 넣을 수 있는 무게의 합을 넘으면 pass

    if C < a_weight:
        continue

    l, r = 0, len(b_sum) - 1
    while l <= r:
        mid = (l + r) // 2

        # 만약 가방에 여유 공간이 있다면, 그보다 더 무거운 물건 조합으로 넣어보기
        if a_weight + b_sum[mid] <= C:
            l = mid + 1

        # 만약 가방에 여유 공간이 없다면, 더 가벼운 물건 조합으로 넣어보기
        else:
            r = mid - 1

    # 가방에 물건을 넣을 수 있는 최대 조건을 찾는 과정이기 때문에, ans += l
    ans += l
        
print(ans)