import sys
def input():
    return sys.stdin.readline().rstrip()

arr = list(map(int, input().split()))

n = len(arr)
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
