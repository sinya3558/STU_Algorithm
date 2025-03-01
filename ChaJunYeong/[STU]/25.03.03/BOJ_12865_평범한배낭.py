import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    n개의 물건에 대한 무게 w와 가치 v에 대한 정보가 주어졌을 때,
    k만큼의 무게를 넘지 않으면서 담을 수 있는 물건 가치의 최댓값 구하기

    코드 참고 : 
    https://velog.io/@keynene/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC5-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-12865-%ED%8F%89%EB%B2%94%ED%95%9C%EB%B0%B0%EB%82%AD
    https://claude-u.tistory.com/208

    냅색 알고리즘
    - 담을 수 있는 물건이 나누어질 수 있는 경우, 분할 가능 배낭 문제 (Fractional Knapsack Problem)
    - 나누어질 수 없는 경우, 0-1 배낭 문제 (0-1 Knapsack Problem)

    풀이 : 다이나믹 프로그래밍 (DP)

    1. 현재 가방에 담길 수 있는 가치의 최댓값을 저장하는 (n + 1, k + 1)인 2차원 배열 arr 생성
    2. arr[y][x]는 최대 x만큼 물건을 가방에 넣을 수 있는 상태에서 y번째 물건을 넣어 보는 것것
        현재 물건의 무게 y_w, 현재 물건의 가치 y_v
        2-1. 현재 물건을 가방에 넣을 수 없는 경우, 이전 물건까지 넣었을 때의 가치, arr[y-1][x] 값과 동일
        2-2. 현재 물건을 가방에 넣을 수 있는 경우,
            - 1. 현재 물건의 가치 + 이전 물건까지 넣었을 때 현재 가방 무게에서 해당 물건을 제외하고 얻을 수 있는 가치의 최댓값
            - 2. 이전 물건까지 넣었을 때 현재 가방 무게에서 얻을 수 있는 가치의 최댓값
            1과 2의 최댓값을 비교, max(y_v + arr[y-1][x - y_w], arr[y-1][x])
"""


n, k = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]

# y축은 현재 넣고자 하는 물건의 index, x는 버틸 수 있는 배낭의 무게
# dp_arr[y][x] 에는 x 무게 만큼 물건을 넣을 수 있는 배낭에서 y 번째 물건을 넣었을 때 얻을 수 있는 가치의 최댓값을 구하는 것
dp_arr = [[0] * (k + 1) for _ in range(n + 1)]

for y in range(1, n + 1):
    for x in range(1, k + 1):

        # 현재 물건의 무게와 가치
        cur_w, cur_v = arr[y-1]

        # 현재 물건을 가방에 넣을 수 있다면,
            # 1. 현재 물건의 가치와 해당 물건 만큼의 무게를 제외하고 이전 물건을 넣었을 때 얻을 수 있는 가치의 최댓값의 합
            # 2. 같은 무게를 이전 물건까지 넣었을 때 가치의 최댓값
        # 1과 2의 최댓값
        if cur_w <= x:
            dp_arr[y][x] = max(cur_v + dp_arr[y-1][x - cur_w], dp_arr[y-1][x])

        # 현재 물건을 가방에 넣을 수 없다면, 같은 무게를 이전 물건까지 넣었을 때 가치의 최댓값
        else:
            dp_arr[y][x] = dp_arr[y-1][x]

print(dp_arr[n][k])