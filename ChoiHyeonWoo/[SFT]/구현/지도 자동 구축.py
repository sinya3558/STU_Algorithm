N = int(input())
start = 2
answer = 0
for i in range(N):
    start += start - 1
answer = start ** 2
print(answer)