# import sys
# sys.stdin = open('input.txt', 'r')

"""
    백준에서 문제 풀다가 시간 초과가 날 경우,
    input 함수를 아래와 같이 바꿔보자.
"""

import sys
def input():
    return sys.stdin.readline().rstrip()

from collections import deque
n = int(input())
q = deque()

for _ in range(n):
    com = input().split()

    # item 넣기기
    if com[0] == "push":
        q.append(com[1])

    # queue 가장 앞에 있는 정수를 제거하면서 출력
    elif com[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)

    # queue size
    elif com[0] == "size":
        print(len(q))

    # queue가 비어있는지 여부 확인
    elif com[0] == "empty":
        if q:
            print(0)
        else:
            print(1)

    # 가장 앞에 있는 정수 출력
    elif com[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
        
    # 가장 뒤에 있는 정수 출력
    elif com[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
    
