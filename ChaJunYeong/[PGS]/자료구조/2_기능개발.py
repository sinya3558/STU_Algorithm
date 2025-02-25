def solution(progresses, speeds):
    answer = []

    """
        00:17:51.460

        큐로 풀이
        1. 우선 각 작업 별로 완성까지 걸리는 시간 측정
        2. 만약, 완성까지 걸리는 시간이 이전 작업보다 오래 걸릴 경우, 이전 작업들 먼저 배포하기
        3. 그렇지 않으면 나중에 배포하기
        4. 마지막에 남은 작업물들 한 번에 배포하기
    """
    
    temp_progress = []
    for i in range(len(progresses)):

        # 1. 각 작업 별로 완성까지 걸리는 시간 측정
        complete_days = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0:
            complete_days += 1
            
        # 2. 만약, 완성까지 걸리는 시간이 이전 작업보다 오래 걸린다면, 이전 작업들을 먼저 배포하기
        if len(temp_progress) != 0 and temp_progress[0] < complete_days:
            answer.append(len(temp_progress))
            temp_progress.clear()

        # 3. 그렇지 않다면, 나중에 배포하기
        temp_progress.append(complete_days)

    if len(temp_progress) != 0:
        answer.append(len(temp_progress))

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
