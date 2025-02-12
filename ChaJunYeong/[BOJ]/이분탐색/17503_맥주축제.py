import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    목표 : 
        가능한 간 레벨을 최소한으로 올리도록 만들기기
       
    조건 : 
        1. 맥주는 하루에 하나씩 마실 수 있음
        2. 이전에 마셨던 맥주는 다시 마실 수 없음
        3. 마시는 맥주 N 개의 선호도 합이 M 이상이 되도록 마시기
"""


"""
    ───── 1차 시도 ─────
    이분탐색으로 해결하려 했으나, 37% 에서 에러 발생
    간과한 것 → 정답이 최대이거나 최소일 경우 정답을 걸러낼 수 있음 
    (l == min_dosu, r == max_dosu 일 경우에도 정답일 수 있음)

    개선 → result = -1로 초기화 한 후, 조건을 만족할 경우에 result = mid로 초기화
"""

n, m, k = map(int, input().split())
beers = [tuple(map(int, input().split())) for _ in range(k)]

min_dosu = min(beers, key=lambda x: x[1])[1]
max_dosu = max(beers, key=lambda x: x[1])[1]

# 선호도가 높은 순으로 정렬한 뒤, 이분탐색으로 찾기
beers.sort(key=lambda x: -x[0])

l, r = min_dosu, max_dosu
result = -1
while l <= r:
    mid = (l + r) // 2
    cnt, pre = 0, 0

    # 맥주 선호도 계산
    for preference, alcohol in beers:
        if alcohol <= mid:
            pre += preference
            cnt += 1
            if cnt == n:
                break
    
    # 1. n일동안 마신 맥주 선호도가 조건을 충족할 경우, r = mid - 1
    # 2. n일동안 마신 맥주 선호도가 낮거나, 맥주를 충분히 마시지 못했을 경우, l = mid + 1
    if cnt == n and m <= pre:
        result = mid
        r = mid - 1
    else:
        l = mid + 1

print(result)
