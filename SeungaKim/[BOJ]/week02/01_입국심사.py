# 7월 2주차 공통문제 
# https://www.acmicpc.net/problem/3079
# 5:41

import sys

# N = 입국심사대 개수, M = 사람수, Get user input
N, M = map(int, input().split())

# N, M 인풋 제한, Check constraint
# if N < 1 or N > 100000:
#     sys.exit()
# if M < 1 or M > 1000000000:
#     sys.exit()
if not (1 <= N <= 100000 and 1 <= M <= 1000000000):
    sys.exit()

# T_k 지정하기, Assign user inputs for T_k(processing time at checkpoints)
T_k = []    # empty list
for _ in range(N):
    T_k.append(int(input()))
# print(T_k)

low = 1
high = max(T_k) * M # worst case scenario, 마지막 사람까지 모두 다 -> 최고 시간 걸리는 심사대 1개일 경우

# Check base
# if high >= low:
#     mid = (high + low) // 2

# initialize minimum time for all M students processed
min_time = 0

while high >= low:
    # initialize mid and number of students passed, BS 중간값과 입국심사 통과된 학생들 수
    mid = (high + low) // 2
    passed_M = 0

    # Iterate through all immigration points to track how many students have passed
    for k in T_k:
        passed_M += mid // k

    # 예상시간보다 더 적게 필요할 경우 BS boundary values 새로 업데이트
    if passed_M >= M:
        min_time = mid
        high = mid - 1
    else:
        # 예상시간 초과한 경우
        low = mid + 1

print(min_time)
