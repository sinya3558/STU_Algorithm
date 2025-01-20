import sys
def input():
    return sys.stdin.readline().rstrip()

# import sys
# sys.stdin = open('input.txt', 'r')


n, m, v = map(int, input().split())
arr = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    arr[s][e] = 1
    arr[e][s] = 1


def dfs():
    isVisited = [False] * (n + 1)
    s = [v]
    
    while s:
        cur_p = s.pop()
        if isVisited[cur_p]:
            continue

        isVisited[cur_p] = True
        print(cur_p, end=" ")

        for next_p in reversed(range(1, n + 1)):
            if not isVisited[next_p] and arr[cur_p][next_p] == 1:
                s.append(next_p)


def bfs():
    from collections import deque
    isVisited = [False] * (n + 1)
    q = deque([v])

    while q:
        cur_p = q.popleft()
        if isVisited[cur_p]:
            continue

        isVisited[cur_p] = True
        print(cur_p, end=' ')

        for next_p in range(1, n + 1):
            if not isVisited[next_p] and arr[cur_p][next_p] == 1:
                q.append(next_p)


dfs()
print()
bfs()
