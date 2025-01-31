import sys
def input():
    return sys.stdin.readline().rstrip()

arr = input().split()
isVisited = [False] * len(arr)

def permutation(temp, depth):
    # 순열이 완성되었으면 출력
    if len(temp) == len(arr):
        print(temp)

    # 그렇지 않으면 하나씩 집어넣기
    # 1. 앞에서부터 하나씩 넣기
    # 2. 이전에 넣었던 요소는 제외
    else:
        for i in range(len(arr)):
            if not isVisited[i]:
                temp.append(arr[i])
                isVisited[i] = True
                permutation(temp, depth + 1)
                temp.pop()
                isVisited[i] = False

permutation([], 0)
