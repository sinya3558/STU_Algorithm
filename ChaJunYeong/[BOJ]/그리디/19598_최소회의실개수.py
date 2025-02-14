import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

"""
    목표 : n개의 회의를 모두 진행할 수 있는 최소 회의실 개수
    조건 : 한 회의실에서 동시에 두 개 이상의 회의가 진행될 수 없음
"""

"""
    1차 시도
    끝나는 시간 → 시작 시간을 기준으로 정렬한 후, 회의실 차례대로 사용
        1. 이전에 사용했던 회의실 중 가장 빨리 끝나는 회의실에 새로운 회의 배정
        2. 만약 사용 가능한 회의실 없다면 새로운 회의실 배정

    4% 에서 에러 발생 → why?
    종료 시간 기준으로 정렬할 경우, 일찍 끝나는 것이 일찍 시작한다는 보장이 없음
    따라서 다음의 경우 에러 발생

    4
    2 3
    1 10
    13 15
    5 20
    Correct : 2
    Wrong : 3
"""

import heapq

# 시작 시간을 기준으로 정렬
meetings.sort(key=lambda x: x[0])

heap = []
heapq.heappush(heap, meetings[0][1]) # 첫 회의 종료 시간으로 초기화

for i in range(1, n):
    cur_s, cur_e = meetings[i]

    # 1. 이전에 사용했던 회의실 중 가장 빨리 끝나는 회의실에 새로운 회의 배정
    if heap[0] <= cur_s:
        heapq.heappop(heap)

    # 2. 그렇지 않으면 새로운 회의실 배정
    heapq.heappush(heap, cur_e)

print(len(heap))
