import sys
from collections import deque
import heapq
input = sys.stdin.readline
N = int(input())
meeting = []
for _ in range(N):
    a, b = map(int, input().split())
    meeting.append((a, b))
meeting.sort(key = lambda x : (x[0], x[1]))
cnt = 1
using = []
now_start, now_end = meeting[0][0], meeting[0][1]
using.append((now_end, now_start))
heapq.heapify(using)
for i in range(1, N):
    temp_start, temp_end = meeting[i][0], meeting[i][1]
    now_end, now_start = heapq.heappop(using)
    if temp_start < now_end:
        cnt += 1
        heapq.heappush(using, (now_end, now_start))
        heapq.heappush(using, (temp_end, temp_start))
    else:
        heapq.heappush(using, (temp_end, temp_start))
print(cnt)