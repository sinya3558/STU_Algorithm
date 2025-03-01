import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    00:04:39.75

    - 참고 자료:
    https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html
    https://littlefoxdiary.tistory.com/3

    우선순위 큐?
        데이터 별로 우선순위가 있고, 
        우선순위가 높은 데이터부터 차레대로 빠져나가게 만드는 자료구조

    힙 (Heap)
        완전 이진 트리의 일종으로 우선 순위 큐를 위해 만들어진 자료 구조
        여러 개의 값들 중 최댓값과 최솟값을 빠르게 찾도록 만들어짐
        힙은 일종의 반정렬 상태 (느슨한 정렬 상태)를 유지하는데,
            예를 들어 최소 힙의 경우, 작은 값이 상위 레벨, 큰 값이 하위 레벨에 있다는 정도만 구분
            그래서 부모 노드의 값이 자식 노드의 값보다 항상 작은 상태만을 유지한다 (자식 노드 끼리의 순서는 고려하지 않음)

        Python에는 기본적으로 heapq (priority queue) 알고리즘을 제공함
            모든 부모 노드는 그의 자식 노드보다 값이 작거나 같은 최소 힙 형태
            - arr : list()
                - heappush(arr, item) : item을 arr에 추가
                - heappop(arr) : arr에서 가장 작은 원소를 pop 하면서 return
                - heapify(arr) : arr을 즉시 heap 자료구조로 변환
            최대 힙으로 활용하고자 하는 경우, item의 값의 부호를 바꿔 저장
"""

n = int(input())
arr = []

import heapq
for _ in range(n):
    x = int(input())

    if   x != 0: heapq.heappush(arr, x)
    elif x == 0:
        if len(arr) != 0: print(heapq.heappop(arr))
        else:             print(0)

    
    print(arr)
