from collections import deque
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr = deque(arr)
max = -1
if len(arr) % 2 == 0:
    i = len(arr) // 2
    for _ in range(i):
        a = arr.pop()
        b = arr.popleft()
        sum = a + b
        if sum > max:
            max = sum
else:
    i = len(arr) // 2
    pop = arr.pop()
    for _ in range(i):
        a = arr.pop()
        b = arr.popleft()
        sum = a + b
        if sum > max:
            max = sum
    if max < pop:
        max = pop
print(max)
        