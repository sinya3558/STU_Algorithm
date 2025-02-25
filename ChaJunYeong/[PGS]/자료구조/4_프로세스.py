def solution(priorities, location):
    answer = 0
    """
        특정 프로세스가 몇 번째로 실행되는지 알아내는 문제

        규칙:
            1. 실행 대기 큐에서 대기 중인 프로세스 꺼내오기
            2. 큐에 대기중인 프로세스보다 우선순위가 더 높은 프로세스가 있다면, 방금 꺼낸 프로세스를 다시 큐에 넣기
            3. 만약 그런 프로세스가 없다면, 방금 꺼낸 프로세스 실행
            4. 한번 실행한 프로세스는 그대로 종료

        00:12:06.440 
            
        Circular Queue로 풀이
        풀이:
            1. 우선 순위대로 프로세스 빼오기 → 우선순위 순으로 프로세스 정렬
            2. 우선순위가 높은 프로세스 순으로 프로세스 실행
                2-1. 만약, 실행해야 할 우선순위와, 현재 프로세스의 우선순위가 동일하다면 슬행
                2-2. 그렇지 않으면, 다음 프로세스로 넘어감 (이때, circular queue이므로 (i+1) % len(priorities))
            3. 만약, 현재 프로세스의 위치와 정답을 원하는 위치, i가 동일하면 answer 출력
    """

    is_visited = [False] * len(priorities)
    sorted_priorities = sorted(priorities, reverse=True)

    i = 0
    for priority in sorted_priorities:

        while True:
            if not is_visited[i] and priorities[i] == priority:
                is_visited[i] = True
                answer += 1
                break

            i = (i + 1) % len(priorities)

        if i == location:
            return answer

print(solution([2, 1, 3, 2]	, 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
