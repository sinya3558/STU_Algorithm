def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i, price in enumerate(prices):
        # 현재 가격보다 큰 가격들을 가진 인덱스는 현재에서 가격 하락을 경험
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    
    # 스택에 남은 인덱스는 끝까지 가격이 떨어지지 않은 경우
    for j in stack:
        answer[j] = n - j - 1
    
    return answer