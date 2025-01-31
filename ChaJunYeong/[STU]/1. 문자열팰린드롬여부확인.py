import sys
def input():
    return sys.stdin.readline().rstrip()

item = input()
flag = True
for i in range(len(item) // 2):
    s = i
    e = len(item) - 1 - i
    if item[s] != item[e]:
        flag = False

print(flag)
