def solution(prices):

    """
        초 단위로 기록된 주식가격이 떨어질 때 까지 걸린 시간 측정

        [1, 2, 3, 2, 3]의 경우
        1. 1은 마지막까지 가격이 떨어지지 않음 (+4)
        2. 2는 마지막까지 가격이 떨어지지 않음 (+3)
        3. 3은 그 다음 2에서 가격이 떨어짐 (+1)
        4. 2는 마지막까지 가격이 떨어지지 않음 (+1)
        5. 3이후에 주식 가격 변동이 없음 (+0)

        00:27:52.108

        풀이:
            스택으로 풀이 - 스택에는 가격과 time stamp에 대한 정보를 저장
            1. 현재 가격이 이전 가격보다 크거나, 스택이 비어있다면 스택에 저장
            2. 현재 가격이 이전 가격보다 작으면 pop
                2-1. 현재 시간과 이전 가격이 들어온 시간 만큼의 차이를 answer에 저장장
            3. 마지막으로 스택에 남아 있는 가격들을 제거 (전체 주식 가격 변동 시간 - 들어온 시간간)
    """

    answer = [0] * len(prices)

    price_stack = []
    for t in range(len(prices)):
        if len(price_stack) == 0:
            price_stack.append((prices[t], t))

        else:
            cur_price = prices[t]
            while True:
                if len(price_stack) == 0 or price_stack[-1][0] <= cur_price:
                    price_stack.append((cur_price, t))
                    break
                
                _, pre_ts = price_stack.pop()
                answer[pre_ts] = t - pre_ts

    for _, pre_ts in price_stack:
        answer[pre_ts] = len(prices) - pre_ts - 1

    return answer


def main():
    print(solution([1, 2, 3, 2, 3]))    # [4, 3, 1, 1, 0]
    print(solution([1, 2, 3, 2, 3, 4, 1]))  # [6, 5, 1, 3, 2, 1, 0]
    print(solution([3, 1])) # [1, 0]


if __name__ == "__main__":
    main()

