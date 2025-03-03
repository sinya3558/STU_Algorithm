import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
objects = []
check_W = deque()
check_V = deque()
for _ in range(N):
    W, V = map(int, input().split())
    objects.append((W, V))
objects.sort(key = lambda x : (x[0], -x[1]))
maximum = -1239339584545
for W, V in objects:
    if W < K:
        maximum = max(maximum, V)
for i in range(len(objects)):
    W, V = objects[i][0], objects[i][1]
    check_W.append(W)
    check_V.append(V)
    signal = 0
    if sum(check_W) > K:
        check_W.pop()
        check_V.pop()
        if not check_W:
            break
        maximum = max(maximum, sum(check_V))
        signal = 1
        check_W.append(W)
        check_V.append(V)
        while sum(check_W) > K:
            check_W.popleft()
            check_V.popleft()
            if not check_W:
                break
if signal == 0:
    maximum = max(maximum, sum(check_V))
print(maximum)