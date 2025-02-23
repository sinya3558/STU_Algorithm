N = int(input())
arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append((a,b))
    
arr = sorted(arr, key = lambda x : (x[1], x[0]))
check = arr[0][1]
cnt = 1
for i in range(1, N):
    if arr[i][0] >= check:
        check = arr[i][1]
        cnt+=1
print(cnt)