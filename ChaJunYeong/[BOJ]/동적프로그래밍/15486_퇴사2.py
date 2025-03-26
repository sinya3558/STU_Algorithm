import sys
def input():
    return sys.stdin.readline().rstrip()


"""
    00:41:32.007

    N + 1 번째 되는날 퇴사하기 위해, 남은 N일 동안 최대한 많은 상담하고자 함
    상담하는데 걸리는 시간을 T, 받을수 있는 금액을 P라고 했을 때,
    최대한 많은 수익을 구하는 프로그램 작성하기

    문제 풀이:
        DP 문제로 풀어야 할 것 같음
        특정 날짜에 받을 수 있는 최대 금액을 저장하는 DP array 선언

        * 풀이 참조 : 
        https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80-15486-%ED%87%B4%EC%82%AC-2


"""

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.insert(0, [0, 0])


dp = [0] * (N + 1)
for start in range(1, N + 1):
    # 일단, 이전 상담 날짜까지 받을 수 있는 상담 금액의 최댓값 넣기
    dp[start] = max(dp[start], dp[start - 1])

    # 해당 날짜에 진행해야 하는 상담 정보 (t : 상담 기간, p : 상담 보상, end : 상담이 끝나는 날짜)
    t, p = arr[start]
    end = start + t - 1

    # 상담이 퇴사일을 넘긴다면 pass
    if N < end: continue

    # 그렇지 않다면, 해당 상담을 마친 날짜에 얻을 수 있는 최대 금액 계산
    #   1. 상담을 진행했다면,       이전 날짜까지 상담하며 받은 금액 + 해당 상담 금액
    #   2. 상담을 진행하지 않았다면, 해당 날짜의 최대 금액
    dp[end] = max(dp[start - 1] + p, dp[end])

print(max(dp))