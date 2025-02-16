N ,M = map(int, input().split())
player = [list(map(int, input().split())) for _ in range(N)]
point = [0] * (N+1)
for k in range(M):
    max_point = [0] * (N+1)
    for i in range(N):
        max_point[i+1] = max(player[i])
        for j in range(M):
            if max(player[i]) == player[i][j]:
                player[i][j] = 0
                break
    for q in range(1, len(max_point)):
        if max(max_point) == max_point[q]:
            point[q] += 1
for i in range(1, len(point)):
    if point[i] == max(point):
        print(i, end = ' ')
    

        

