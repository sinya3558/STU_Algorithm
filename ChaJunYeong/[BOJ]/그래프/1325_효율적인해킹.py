import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
relation = {i:[] for i in range(n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    relation[b].append(a)

# 1. 1번 컴퓨터부터 n번 컴퓨터까지 해킹 시작
# 2. 해킹된 컴퓨터를 신뢰하는 컴퓨터들 확인
#   2-1. ★ 만약 이전에 방문한 적이 있으면 queue에 넣지 않음
#   2-2. ★ 만약 이전에 방문한 적이 없으면 queue에 넣고 hacking 했다고 알림
# 3. 해킹된 컴퓨터 확인
# 4. max값 확인 후 정답 초기화

result = []
max_hack = -1

from collections import deque
for i in range(1, n+1):
    q = deque()
    isHacked = [False] * (n + 1)
    
    q.append(i)
    isHacked[i] = True
    while q:
        cur_hack = q.popleft()
        for next_com in relation[cur_hack]:
            if not isHacked[next_com]:
                q.append(next_com)
                isHacked[next_com] = True
    cnt = isHacked.count(True)

    if max_hack < cnt:
        result = [i]
        max_hack = cnt
    elif max_hack == cnt:
        result.append(i)

print(*result)
