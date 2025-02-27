def solution(numbers, target):

    """
        00:08:53.32

        numbers의 숫자들을 적절히 더하거나 빼서 target number로 만들 수 있는 방법 찾기
        조건 : numbers 내부의 모든 숫자를 다 사용해야 함

        풀이 :
            깊이 우선 탐색 (DFS)로 풀이
            1. 각 숫자별로 + / - 부여
            2. 마지막까지 부호를 부여했을 때, target number를 만들 수 있는지 확인
    """
    answer = 0

    def dfs(depth, operators):
        nonlocal answer

        if depth == len(numbers):
            make_target = 0
            for op, num in zip(operators, numbers):
                if   op == '-': make_target -= num
                elif op == '+': make_target += num

            if make_target == target: answer += 1
            return
        
        else:
            for op in ['+', '-']:
                operators.append(op)
                dfs(depth + 1, operators)
                operators.pop()

    dfs(0, [])
    return answer



# def solution(numbers, target):
#     # 개인적으로 nonlocal, global을 사용하는 방식은 좋지 않은 것 같음

#     def dfs(depth):
#         answer = 0
#         if depth == len(numbers):
#             if sum(numbers) == target: return 1
#             else: return 0

#         else:
#             answer += dfs(depth + 1)
#             numbers[depth] *= -1    # 부호 바꾸기
#             answer += dfs(depth + 1)
#             return answer

#     return dfs(0)



def main():
    print(solution([1, 1, 1, 1, 1], 3))
    print(solution([4, 1, 2, 1], 4))


if __name__ == "__main__":
    main()