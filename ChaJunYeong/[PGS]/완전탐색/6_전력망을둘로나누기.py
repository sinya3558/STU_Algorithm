def solution(n, wires):

    """
        00:55:45.07

        n개의 송전탑이 전선을 통해 트리 형태로 연결되어 있음
        이 전선들 중 "하나"를 끊어 현재 전력망 네트워크를 2개로 분할하고자 함
        이때, 두 젼력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추기
        두 전력망이 가지고 있는 송전탑 개수의 차이 (절댓값)를 구하는 것이 목표

        끊어진 트리 탐색은 너비우선탐색으로 진행
        그 전 아이디어는 연결된 송전탑 개수가 많은 송전탑의 전선을 먼저 끊어보는 것이 목표
        1. graph와 연결된 전선이 많은 순으로 정렬
        2. 해당 송전탑과 연결된 전선을 끊기
            2-1. 해당 송전탑과 연결된 송전탑 개수 확인
            2-2. 전선을 끊었을 때, 다른 트리에 연결된 송전탑 개수 확인
            2-3. 송전탑 개수 업데이트
    """

    graph = {i:[] for i in range(1, n + 1)}
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    sorted_graph = sorted(graph.items(), key=lambda x: -len(x[1]))


    # 끊어진 트리에서 연결된 노드 갯수 확인
    from collections import deque
    def check_tree(v1, v2):         # v1은 확인하려는 노드, v2는 끊어진 노드
        visited = [False] * (n + 1) # 이미 방문한 노드인지 확인하는 용도
        visited[v1] = True
        visited[v2] = True
        q = deque([v1])
        cnt = 1

        while q:
            cur_node = q.popleft()
            for next_node in graph[cur_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append(next_node)
                    cnt += 1
        return cnt
    

    answer = n
    visited = [[False] * (n + 1) for _ in range(n + 1)] # 한번 끊어진 노드인지 확인하는 용도
    for node, edges in sorted_graph:
        for edge in edges:

            # 정답이 이미 최솟값에 도달했으면 break
            if answer == 0:
                break

            # 한 번 끊어진 노드가 아니라면 연결된 트리들 계산해보기
            # 한 개의 트리의 노드 개수가 정해지면 (cnt), 자동적으로 반대쪽 트리의 노드 개수가 정해짐 (n-cnt)
            if not visited[node][edge]:
                visited[node][edge] = True
                visited[edge][node] = True
                cnt = check_tree(node, edge)
                answer = min(answer, abs(n - cnt - cnt))

    return answer



# def solution(n, wires):
#     ans = n
#     for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
#         s = set(sub[0])
#         [s.update(v) for _ in sub for v in sub if set(v) & s]
#         ans = min(ans, abs(n - len(s) - len(s)))
#     return ans



def main():
    print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))   # 3
    print(solution(4, [[1,2],[2,3],[3,4]])) # 0
    print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))   # 1
    print(solution(13, [[1, 2], [2, 3], [3, 9], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 10], [10, 11], [11, 12], [12, 13]]))    # 1


if __name__ == "__main__":
    main()
