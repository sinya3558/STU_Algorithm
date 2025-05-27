# 공통문제 레벨 : 실버 3이상
# https://www.acmicpc.net/problem/25401
# 1:17
'''
입력 1 
4
1 2 2 4

출력 1 
1
(1 2 3 4)

입력 2 
5
6 3 3 1 -1

출력 2 
2 
(7 5 3 1 -1)
'''
import sys

N = int(input())

if not 2 <= N <= 500:
    sys.exit()  # out of range (N)

deck = list(map(int, input().split()))  # 유저 인풋값 넣은다음

for x_i in deck: 
    if not -1000000 <= x_i <= 1000000:
        sys.exit()  # out of range (user input for cards)

''' 조건 : 
    (1) 규칙적으로 증가: +d
    (2) 감소 : -d
    (3) 일정: d = 0 
    => 최소 변화로 카드덱 등차수열 만들어 버리기 '''

# count_inc = 0
# count_dec = 0
# count_equal = 0
d = 0
list_d = [0]*(N * (N-1))
for i in range(N):
    for j in range(N):  # *** for j in range(1, N): 하지마라 바보야. i != 0 인 경우 인덱스 0 취급 안히고 넘어감. **
        d = deck[j] - deck[i]
        list_d.append(d)

dict_d = {}
for d in list_d:
    if d in dict_d:
        dict_d[d] += 1

# max nums of d = best d(공차값)
best_d = max(dict_d, key=dict_d.get)        

# 4:50