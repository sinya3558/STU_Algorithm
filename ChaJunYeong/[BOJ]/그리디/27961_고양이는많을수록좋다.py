import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    1. 처음에는 고양이 없음1
    2. 생성 : 고양이 1마리 생성
    3. 복제 : 고양이 일부 또는 전부를 대상으로 복제
        3-1. 만약 k마리 존재한다면 0마리 이상 k마리 이하의 고양이 추가 가능
    - 이를 적절히 사용해 최소 행동 횟수로 정확히 n마리의 고양이가 있도록 만들기

    생성된 고양이는 정확히 n이 될 필요가 없음.
    3번 규칙에 의해, n보다 작은 수 이기만 하면 됨
"""

n = int(input())

cnt = 0
cat = 0
while True:
    if n <= cat:
        break

    if cat == 0: cat += 1
    else:        cat *= 2
    cnt += 1

print(cnt)
