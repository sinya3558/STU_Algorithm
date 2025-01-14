import sys
M = int(input())
S = []
for _ in range(M):
    temp = sys.stdin.readline().strip().split()
    if temp[0] == 'all':
        S.clear()
        for i in range(1, 21):
            S.append(i)
        continue
    if temp[0] == 'empty':
        S.clear()
        continue
    temp[1] = int(temp[1])
    if temp[0] == 'add':
        if temp[1] not in S:
            S.append(temp[1])
    elif temp[0] == 'remove':
        if temp[1] in S:
            S.remove(temp[1])
    elif temp[0] == 'check':
        if temp[1] in S:
            print(1)
        else:
            print(0)
    elif temp[0] == 'toggle':
        if temp[1] in S:
            S.remove(temp[1])
        else:
            S.append(temp[1])