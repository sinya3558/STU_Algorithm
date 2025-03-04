import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    
    day = [math.ceil((100 - x) / y) for x, y in zip (progresses, speeds)]
    n = deque(day)
    
    while n:
        deploy_day = n.popleft()
        count = 1
        while n and n[0] <= deploy_day:
            n.popleft()
            count += 1
        answer.append(count)
    return answer