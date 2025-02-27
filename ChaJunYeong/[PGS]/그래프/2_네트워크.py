from collections import deque

def solution(n, computers):

    """
        00:07:38.24

        네트워크의 갯수 찾기

        풀이 : 
            너비 우선 탐색으로 풀이
            1. 방문하지 않은 컴퓨터를 기준점으로 queue에 넣기
            2. queue에 넣어진 컴퓨터와 연결된 컴퓨터를 queue에 넣기
                2-1. 이때, 한번도 방문하지 않은 컴퓨터여야 함
    """
    answer = 0

    visited = [False] * n
    for i in range(n):
        # 방문하지 않은 컴퓨터를 기준으로 잡기
        if visited[i]: continue

        # 해당 노드의 컴퓨터와 연결된 컴퓨터들 찾기
        # 조건 1 : 연결되어 있어야 함
        # 조건 2 : 한 번도 방문하지 않은 컴퓨터여야 함
        q = deque([i])
        visited[i] = True
        while q:
            cur_node = q.popleft()
            for next_node in range(n):
                if computers[cur_node][next_node] == 1 and not visited[next_node]:
                    q.append(next_node)
                    visited[next_node] = True
        answer += 1

    return answer



def main():
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))


if __name__ == "__main__":
    main()