import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    0의 경우, 1 / 0
    1의 경우, 0 / 1
    2의 경우, 1 / 1 (1 + 0)
    3의 경우, 1 / 2 (2 + 1)
    4의 경우, 2 / 3 (3 + 2)
    5의 경우, 3 / 5 (4 + 3)
    6의 경우, 5 / 8 (5 + 4)
    ...

    피보나치 수열을 계산하되, f(n-1), f(n-2)의 결과를 차례대로 출력
"""

def test_case(n):
    if   n == 0:
        return [1, 0]
    elif n == 1:
        return [0, 1]
    else:
        arr = [0] * n
        arr[0] = 1
        arr[1] = 1
        for i in range(2, n):
            arr[i] = arr[i-1] + arr[i-2]
        return [arr[n-2], arr[n-1]]

T = int(input())
for _ in range(T):
    n = int(input())
    print(*test_case(n))