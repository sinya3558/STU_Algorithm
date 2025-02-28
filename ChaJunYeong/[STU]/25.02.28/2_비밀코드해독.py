def solution(n, q, ans):

    """
        비밀 조직의 보안 시스템 해독

        조건 1 : 시스템은 1~n 까지 중 서로 다른 정수 5개가 오름차순으로 정렬되어 있음
        조건 2 : 총 m 번의 시도 가능
        조건 3 : 서로 다른 5개의 정수를 입력하면 그 중 몇 개가 비밀 코드에 포함되어 있는지 알려줌

        지금까지 시도를 q, 그에 따라 몇 개의 비밀 코드가 포함되어 있는지 ans로 알려준다고 하면
        위 조건을 만족하는 비밀 코드 조합 갯수 찾기

        10 <= n <= 30

        풀이 : 
            백트래킹으로 해결
                1. 1 부터 숫자를 점점 키워나가면서 하나씩 집어 넣기
                2. 이때, 숫자를 넣었을 때, 일치하는 갯수 또한 updqte
                3. 만약, 숫자를 넣었을 때, 일치하는 정답 개수가 ans보다 크다면 break
                4. 만약, 5개 까지 넣었을 때, ans 리스트와 일치하면 정답 + 1
    """

    answer = 0
    visited = [False] * (n + 1)
    visited[0] = True

    def dfs(num_lst, ans_lst):
        nonlocal answer

        if len(num_lst) == 5:
            if ans == ans_lst:
                answer += 1
                return
            
        else:
            # 현재 오름차순의 기준이 되는 숫자
            cur_num = 0 if len(num_lst) == 0 else num_lst[-1]

            # 한 번도 사용하지 않았던 숫자 조합 확인
            for i in range(cur_num + 1, n + 1):
                if not visited[i]:

                    # 만약, 해당 숫자가 기존 암호 해독 코드 힌트에 포함되어 있으면 + 1
                    # 근데, 일치하는 개수를 초과하게되면 false
                    good_num = True
                    next_ans_lst = ans_lst[:]
                    for m in range(len(q)):
                        if i in q[m]:
                            next_ans_lst[m] += 1
                        if ans[m] < next_ans_lst[m]:
                            good_num = False
                            break

                    # 그렇지 않으면 다음 조합 확인
                    if good_num:
                        visited[i] = True
                        num_lst.append(i)
                        dfs(num_lst, next_ans_lst)
                        visited[i] = False
                        num_lst.pop()
                
    dfs([], [0] * len(q))
    return answer



def main():
    print(solution(10, [[1, 2, 3, 4, 5]], [5]))
    print(solution(10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]))
    print(solution(15, [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]], [2, 1, 3, 0, 1]))



if __name__ == "__main__":
    main()