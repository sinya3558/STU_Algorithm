# 19939 박 터트리기
# 5:38
'''
N개의 공을 K개의 가방에 나누어 담을 것,
각 가방에는 1개 이상 담아야 하고, 가방에 담긴 공의 수는 모두 다르게 해야 함
이때 공을 나눌 수 없으면 -1 아웃풋 / 나눌 수 있다면 가장 많이 담긴 가방과 가장 적게 담긴 가방의 차이가 아웃풋
'''
# range(start, stop(***excluded itself***), step)

import sys

N, K = map(int, input().split())

if not 2 <= N <= 100000:
    sys.exit()
elif not 2<= K <= 1000:
    sys.exit()
else:
    k_bags = [ i+1 for i in range(0, K, 1)] # 0 ~ K-1
    count_balls = N - sum(k_bags)
            
    if count_balls < 0:
        print(-1) 
    else:
        # ✅코드참조 : 동일한 개수의 공 처리하는 부분 코드 참조함! ==> 공 개수 많은 가방부터 남은 공 추가해야하고 중복 피하려면 가방안에 있는 공의 개수 비교하는 구문 있어야함 
        left_balls = count_balls
        # for i in range(K-1, -1, -1):   # reverse order to avoid duplicate ball counts in the bags , 담부턴 그냥 list[0] 비워두고 무시하고 인덱스 1, K+1 할 것
        #     if left_balls == 0:
        #         break
        #     k_bags[i] += 1
        #     left_balls -= 1
        #     # print(k_bags)

        reverse_idx = K-1
        while left_balls > 0 :
            # ✅공 개수 중복일때(**** 얘가 너무 어려웠다 **** line 37 ~ 40)
            # ✅ 먼저 index 검사! out of range 방지
            if reverse_idx < K - 1 and k_bags[reverse_idx] + 1 == k_bags[reverse_idx + 1]:
                reverse_idx -= 1
                if reverse_idx < 0: # 한바퀴 다 돌았을때 리셋
                    reverse_idx = K-1
            else:
                k_bags[reverse_idx] += 1    # 중복아닌경우 공 추가
                left_balls -= 1
                reverse_idx -= 1
                # print(k_bags)
                if reverse_idx < 0: # 한바퀴 다 돌았을때 리셋222
                    reverse_idx = K-1
            
        print(max(k_bags) - min(k_bags))