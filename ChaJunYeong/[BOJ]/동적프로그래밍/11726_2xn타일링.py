import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    2xn 타일링 → 피보나치 문제랑 다를바가 없음
    (가로가 n 인 경우의 수 = 가로가 n-1 인 경우의 수 + 가로가 n-2 인 경우의 수)
"""

n = int(input())
arr = [0] * 1001
arr[0] = 1
arr[1] = 1

def fibo(n):
    for i in range(2, n + 1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n] % 10007
    
print(fibo(n))
