import sys
input = sys.stdin.readline
N = int(input())
bridge = list(map(int, input().split()))
start = 0
check = []
while start != N-1:
    K = 3495834598340
    for i in range(start+1, N):
        power = (i - start) * (1 + abs(bridge[start] - bridge[i]))
        if K > power:
            start = i
            K = power
print(check)
print(min(check))