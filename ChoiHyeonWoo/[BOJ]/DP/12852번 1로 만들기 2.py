import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
arr = [N]
while 1:
    test = 0
    if N == 1:
        print(cnt)
        for x in arr:
            print(x, end = ' ')
        break
    test_N = str(N)
    for x in test_N:
        x = int(x)
        test += x
    if test % 3 == 0:
        cnt += 1
        N //= 3
        arr.append(N)
    elif int(test_N[-1]) % 2 == 0:
        cnt += 1
        N //= 2
        arr.append(N)
    else:
        cnt += 1
        N -= 1
        arr.append(N)