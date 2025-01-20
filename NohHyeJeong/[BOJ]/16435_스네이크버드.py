N, L = input().split()
h = list(map(int, input().split()))

N, L = int(N), int(L)
h.sort()


if int(N) == len(h):
    for i in h:
        if i <=L:
            L += 1    
print(L)


'''
    음수 양수 조건 추가하지 않았는데 맞았다고 한다.
    이럴거면 왜 인풋 값 리미트 조건을 붙인거지
'''