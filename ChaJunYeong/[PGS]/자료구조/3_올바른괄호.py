def solution(s):
    answer = True
    
    # 일단, 입력받은 문자열이 짝수가 아니면 정답이 아님
    if len(s) % 2 != 0:
        return False
    
    """
        00:05:07.880
       
        스택으로 풀이
        1. 마지막에 입력받은 문자와 현재 문자가 한 쌍을 이룬다면 pop
        2. 그렇지 않으면 스택에 저장
        3. 최종적으로 스택이 비었으면 True, 그렇지 않으면 False
    """

    temp_s = []
    for i in range(len(s)):
        # 1. 마지막에 입력받은 문자와 현재 문자가 한 쌍을 이룬다면 pop
        if len(temp_s) != 0 and temp_s[-1] == "(" and s[i] == ")":
            temp_s.pop()
            
        # 2. 그렇지 않으면 스택에 저장
        else:
            temp_s.append(s[i])

    # 3. 최종적으로 스택이 비었으면 True, 그렇지 않으면 False
    return True if len(temp_s) == 0 else False


print(solution("()()"))
