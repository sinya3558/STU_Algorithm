def solution(arr):
    answer = []
    for current in arr:
        if not answer or answer[-1] != current:
            answer.append(current)

    return answer