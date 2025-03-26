import sys
def input():
    return sys.stdin.readline().rstrip()
 
"""
    00:38:30.09

    정수 x에 사용할 수 있는 연산

        1 : x가 3으로 나누어 떨어지면 3으로 나누기
        2 : x가 2로 나누어 떨어지면 2로 나누기
        3 : 1 빼기

    위 3가지 방법을 적절하게 사용해서 1로 만들고자 할 때,
    연산을 사용하는 횟수의 최솟값 출력

    풀이 : 
        징검다리 건너기와 비슷한 것 같음
        dp_arr을 만들어서 해당 숫자를 만들기 위한 최솟값 기록하기
        track_arr에는 최솟값으로 선택된 숫자 기록하기

        예를 들어, n = 10으로 주어질 경우
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        9부터 거꾸로 탐색
        9의 경우, 9*2=18, 9*3=27은 10을 벗어나므로 제외, 9+1 연산 사용 가능하므로 가능한 연산 arr[10] + 1 = 1
        8의 경우, 8*2=16, 8*3=24은 10을 벗어나므로 제외, 8+1 연산 사용 가능하므로 가능한 연산 arr[9] + 1 = 2
        7의 경우, 7*2=14, 7*3=21은 10을 벗어나므로 제외, 7+1 연산 사용 가능하므로 가능한 연산 arr[8] + 1 = 3
        6의 경우, 6*2=12, 6*3=18은 10을 벗어나므로 제외, 6+1 연산 사용 가능하므로 가능한 연산 arr[7] + 1 = 4
        5의 경우, 5*3=15는 10을 벗어나므로 제외, 5*2=10, 5+1=6 중 연산의 최솟값에 + 1, min(arr[10], arr[6]) + 1 = 1
        4의 경우, 4*3=12는 10을 벗어나므로 제외, 4*2=8, 4+1=5 중 연산의 최솟값에 +1, min(arr[8], arr[5]) + 1 = 2
        3의 경우, 3*3=9, 3*2=6, 3+1=4 중 연산의 최솟값에 +1, min(arr[9], arr[6], arr[4]) + 1 = 2
        2의 경우, 2*3=6, 2*2=4, 2+1=3 중 연산의 최솟값에 +1, min(arr[6], arr[4], arr[3]) + 1 = 3
        1의 경우, 1*3=3, 1*2=2, 1+1=2 중 연산의 최솟값에 +1, min(arr[3], arr[2]) + 1 = 3
"""

# 입력
n = int(input())
dp = [0] * (n + 1)
track = [0] * (n + 1)

for cur_num in range(n-1, 0, -1):

    # 1. 현재 값에서 세 방법으로 모두 연산, 이때 연산 값이 n보다 커지는 경우 pass
    nxt_nums = []
    for op, num in [('*', 3), ('*', 2), ('+', 1)]:
        if   op == '*': nxt_num = cur_num * num
        elif op == '+': nxt_num = cur_num + num
        if nxt_num <= n:
            nxt_nums.append(nxt_num)

    # 2. 현재 값을 만들 수 있는 숫자의 최솟값 기록하기 
    min_idx = 0
    min_num = sys.maxsize
    for nxt_num in nxt_nums:
        if dp[nxt_num] <= min_num:
            min_idx = nxt_num
            min_num = dp[nxt_num]
    dp[cur_num] = min_num + 1
    track[cur_num] = min_idx

# 출력
answer = [1]
while True:
    if answer[-1] == n:
        answer = answer[::-1]
        break
    answer.append(track[answer[-1]])
print(dp[1])
print(*answer)