import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))

"""
    입력 조건 : 
        - 돌의 최댓값 5,000
        - 힘의 최댓값 100,000

    완전 탐색으로 풀이할 경우,
    현재 있는 돌에서 힘이 최소가 되는 돌로 넘어갈 수 있음
    이때, 최악의 경우, 모든 돌을 밟으면서 이동하는 경우가 발생할 수 있는데, 이때 시간 복잡도는 O(n^2)

    이분 탐색으로 풀이하면, 
    돌을 넘어가는데 드는 힘의 최솟값을 찾을 때 까지 반복
    1. 돌을 건널 수 있다면, 최솟값을 구헤야 하므로 r = mid - 1
    2. 돌을 건널 수 없다면, (즉, 힘이 부족하다면) l = mid + 1

    첫번째 시도 : 2%에서 에러 발생
        → 건널 수 있는 돌에 제한을 둔 것이 문제인 듯
        → 아무리 봐도 잘 모르겠어서 코드 참고

    https://limecoding.tistory.com/241
    
    보다보니 기존 풀이의 경우, 바로 다음 돌로 갈 수 있으면 해당돌로 이동만 했음
    갈 수 있는 모든 경우의 수를 열어두고, 마지막 돌로 움직일 수 있는지 판단했어야 했음
"""


l, r = 1, (n-1) * (1 + abs(arr[-1] - arr[0]))

while l <= r:
    # 현재 사용할 수 있는 힘의 크기
    mid = (l + r) // 2

    # 다음 돌로 이동할 수 있는지 확인하기 
    # (이때, 이미 방문했던 돌은 제외, 어차피 해당 돌로 이동하면 결과는 똑같이 나올 것임. 반복 계산을 막기 위함)
    visited = [False] * n
    visited[0] = True
    can_move_stones = [0]
    can_move = False

    # 돌을 하나씩 꺼내면서 다음 돌로 이동할 수 있는 돌을 모두 넣기
    while len(can_move_stones) != 0:
        cur_pos = can_move_stones.pop()
        if cur_pos == n-1:
            can_move = True
            break

        for next_pos in range(cur_pos + 1, n):
            k = (next_pos - cur_pos) * (1 + abs(arr[next_pos] - arr[cur_pos]))
            if not visited[next_pos] and k <= mid:
                visited[next_pos] = True
                can_move_stones.append(next_pos)

    # 만약 이동할 수 있으면 힘을 더 줄여서 확인
    if can_move:
        r = mid - 1
    # 만약 돌을 모두 꺼냈음에도 불구하고 이동할 수 없으면 힘을 더 늘려서 확인
    else:
        l = mid + 1

print(l)
    