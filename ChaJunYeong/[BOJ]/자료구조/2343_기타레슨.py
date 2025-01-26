import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = list(map(int, input().split()))

"""
    주어진 블루레이를 모두 사용할 필요 없음 (즉, 생성된 블루레이 갯수가 목표량보다 작아도 됨)

    1단계 
    블루 레이 길이 후보군으로 실제 블루 레이 생성
    현재까지 생성된 블루레이 길이에 다음 강의 넣기
    1. 생성된 블루레이 길이가 목표 블루 레이 길이 (mid) 보다 작으면 추가
    2. 생성된 블루레이 길이가 목표 블루 레이 길이 (mid) 보다 크면
        2-1. 블루레이 길이 (temp_blueray) 현재 강의 길이 (length) 로 초기화
        2-2. 블루레이 갯수 (cnt_blueray) 1 추가

    2단계
    1. cnt_blueray가 목표량(m) 보다 같거나 작으면, 길이를 줄여야 함
    2. cnt_blueray가 목표량(m) 보다 크면, 길이를 늘려야 함 
"""

l = max(arr) # 블루 레이 최소 길이
r = sum(arr) # 블루 레이 최대 길이

while l <= r:
    mid = (l + r) // 2 # 블루 레이 길이 후보

    # 1단계
    cnt_blueray = 1
    temp_blueray = 0
    for length in arr:
        if temp_blueray + length <= mid:
            temp_blueray += length
        else:
            temp_blueray = length
            cnt_blueray += 1

    # 2단계
    if cnt_blueray <= m:
        r = mid - 1
    elif m < cnt_blueray:
        l = mid + 1

# 최종적으로 나온 결과값은, 블루레이 길이를 더이상 줄일 수 없을 때 나옴
# 블루 레이 최소 길이 (l)가 정답값이 됨
print(l)
