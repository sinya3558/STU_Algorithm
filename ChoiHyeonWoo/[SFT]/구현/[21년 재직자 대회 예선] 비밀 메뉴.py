import sys
M, N, K = map(int, input().split())
secret = list(map(int, input().split()))
button = list(map(int, input().split()))
if len(secret) > len(button):
    print('normal')
    sys.exit()
sign = 0
for i in range(len(button)):
    if button[i] == secret[0]:
        if button[i:i + len(secret)] == secret:
            sign = 1
            print('secret')
            break
    if len(button) - i < secret:
        break
if sign == 0:
    print('normal')