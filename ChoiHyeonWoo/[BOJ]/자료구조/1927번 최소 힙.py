import heapq
import sys
input = sys.stdin.readline
N = int(input())
a = []
answer = []
for _ in range(N):
    x = int(input())
    if x > 0:
        answer.append(heapq.heappush(a, x))
    elif x == 0:
        if not a:
            # print(0)
            answer.append(0)
            continue
        # print(heapq.heappop(a))
        answer.append(heapq.heappop(a))
for x in answer:
    if x == None:
        continue
    print(x)