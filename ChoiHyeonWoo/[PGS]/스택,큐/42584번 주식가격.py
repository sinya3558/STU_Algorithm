def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        now = prices[i]
        cnt = 0
        for j in range(i+1, len(prices)):
            if now > prices[j]:
                cnt += 1
                break
            cnt += 1
        answer.append(cnt)
    answer.append(0)
    return answer