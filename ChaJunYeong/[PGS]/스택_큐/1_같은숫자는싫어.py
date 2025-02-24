def solution(arr):

    """
        00:02:50.300
        
        스택으로 풀이
        1. 마지막에 들어간 숫자와 값이 똑같다면 넘어가기
        2. 마지막에 들어간 숫자와 값이 다르다면 넣기
    """

    answer = []
    for value in arr:
        if len(answer) != 0 and answer[-1] == value:
            continue
        
        answer.append(value)
    return answer