N, K = map(int, input().split())
HP = list(map(str, input()))
cnt = 0
for i in range(len(HP)):
    if HP[i] == 'P':
        for j in range(i-K, i):
            if j >= 0:
                if HP[j] == 'H':
                    HP[j] = 'C'
                    cnt+=1
                    break
        else:
            for k in range(i+1, i+K+1):
                if k < N:
                    if HP[k] == 'H':
                        HP[k] = 'C'
                        cnt+=1
                        break
print(cnt)