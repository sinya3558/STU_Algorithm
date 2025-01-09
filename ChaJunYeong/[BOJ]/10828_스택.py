# import sys
# sys.stdin = open('input.txt', 'r')

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
stack = [0] * 10000

"""
    stack 내부에 직접 item을 제거하는 것이 아니라
    size pointer를 통해 가장 위에 올라가 있는 item을 바꾸는 방법
"""
 
size = 0

for _ in range(n):
    com = input().split()

    # stack에 정수 넣기
    if com[0] == "push":
        stack[size] = com[1]
        size += 1

    # stack 맨 위에 올라와 있는 정수 빼기
    elif com[0] == "pop":
        if size == 0:
            print(-1)
        else:
            print(stack[size-1])
            size -= 1

    # stack 크기
    elif com[0] == "size":
        print(size)

    # stack 비어있는지 여부
    elif com[0] == "empty":
        if size == 0:
            print(1)
        else:
            print(0)

    # 맨 위의 item 찾기
    elif com[0] == "top":
        if size == 0:
            print(-1)
        else:
            print(stack[size-1])