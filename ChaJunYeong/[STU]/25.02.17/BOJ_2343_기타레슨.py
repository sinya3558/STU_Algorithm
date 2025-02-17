import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    블루레이에는 총 N개의 강의가 들어가야함. 이때, 강의 순서는 바뀌면 안됨. 
    (즉, i번 강의와 j번 강의를 같은 블루레이에 녹화하려면 그 사이 모든 강의 또한 같이 녹화해야함)
    M개의 같은 크기의 블루레이에 모든 기타 강의 동영상을 녹화.
    이때, 블루레이의 크기, 즉 녹화 가능한 길이를 최소로 하려고 함.

    목표 : 가능한 최소 크기의 블루레이 길이 구하기
    조건 : 
        - 모든 블루레이의 크기는 같아야 함
        - 강의의 순서는 바뀌면 안됨

    예시 : 
        Input : 
            9 3
            1 2 3 4 5 6 7 8 9
        Output : 
            17 (1, 2, 3, 4, 5 = 15 / 6, 7 = 13 / 8, 9 = 17)
"""

n, m = map(int, input().split())
bluerays = list(map(int, input().split()))


"""
    풀이 : 

    강의 순서를 바꿀 수 없기 때문에, 처음부터 찍을 영상 길이를 정해두고 영상 길이를 초과하지 않는 선에서 블루레이에 강의를 최대한 녹화해야 함
    이렇게 녹화된 블루레이 갯수가 m보다 같거나 작으면 해당 녹화 길이를 사용할 수 있음
    이때, 가능한 녹화 길이의 최댓값은 100,000 * 10,000 이므로 완전 탐색으로 최솟값을 구하는 것은 거의 불가능에 가까움
    따라서 이분탐색으로 가능한 최소 길이를 탐색해가야 함
"""

min_blueray, max_blueray = max(bluerays), sum(bluerays)

while min_blueray <= max_blueray:
    # 녹화 가능한 블루레이 크기
    mid = (min_blueray + max_blueray) // 2

    # 블루레이 녹화
    cnt = 1
    cur_blueray = 0
    for time in bluerays:

        # 현재 강의를 찍었을 때, 녹화 가능 크기를 초과하지 않으면 그대로 찍음
        if time + cur_blueray <= mid:
            cur_blueray += time
        
        # 녹화 가능한 크기를 초과한다면, 새로운 블루레이로 녹화
        elif mid < time + cur_blueray:
            cur_blueray = time
            cnt += 1

    # 만약, 녹화된 블루레이의 개수가 목표 수량 (m)보다 같거나 작으면, 그보다 더 작은 길이로 찍어봄 (최솟값을 구해야 하기 때문)
    if cnt <= m:
        max_blueray = mid - 1

    # 만약, 녹화된 블루래이의 개수가 목표 수량 (m)보다 크다면, 블루레이 녹화 크기를 늘려야 함
    elif m < cnt:
        min_blueray = mid + 1

# 이분 탐색을 완료했을 때, 최종적으로 블루레이 길이를 더 줄일 수 없음
# 따라서 min_blueray가 최종답이 됨
print(min_blueray)
