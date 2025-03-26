#최소 힙 : 가장 작은 값을 찾을 때 시간을 줄일 수 있는 자료구조
#완전 탐색은 O(n), 최소 힙은 O(log n)이 걸림.
import heapq
import sys
input = sys.stdin.readline
N = int(input())
arr = []
answer = []
for _ in range(N):
    x = int(input())
    #만약 x가 0보다 크면 출력해야 할 리스트 answer에 삽입
    if x > 0:
        answer.append(heapq.heappush(arr, x))
    #x가 0이고 arr이 비었다면 0을 출력할 수 있도록 answer에 0 추가
    elif x == 0:
        if not arr:
            answer.append(0)
            continue
        #x가 0이고, arr이 있다면 heappop
        answer.append(heapq.heappop(arr))
for x in answer:
    if x == None:
        continue
    print(x)


#번외 --> 최대 힙 : 최대값을 빠르게 찾는 법. 파이썬에서 최대힙을 지원하지
#않기 때문에 나름의 꼼수(?)를 쓴다.
for _ in range(N):
    x = int(input())
    # '-'를 붙여주면 된다.
    x *= -1
    if x > 0:
        answer.append(heapq.heappush(arr, x))
    elif x == 0:
        if not arr:
            answer.append(0)
            continue
        answer.append(heapq.heappop(arr))
for x in answer:
    if x == None:
        continue
    #출력할 때 다시 '-'붙여주면 최대 힙 가능.
    print(-x)