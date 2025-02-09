K, P, N = map(int, input().split())
answer = int(pow(K, P * N, 1000000007))
print(answer)