import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while 1:
        check1 = heapq.heappop(scoville)
        if check1 >= K:
            break
        if not scoville:
            return -1
        check2 = heapq.heappop(scoville)
        shake = check1 + (check2 * 2)
        cnt += 1
        heapq.heappush(scoville, shake)
    return cnt