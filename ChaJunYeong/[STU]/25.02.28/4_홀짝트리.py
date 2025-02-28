from collections import deque

def solution(nodes, edges):

    """
        루트 노드가 설정되지 않은 트리가 있음. 모든 노드는 서로 다른 번호를 가짐.
        각 노드는 다음 중 하나 (0은 짝수)
            - 홀수 노드 : 노드 번호가 홀수 + 자식 노드의 개수가 홀수
            - 짝수 노드 : 노드 번호가 짝수 + 자식 노드의 개수가 짝수
            - 역홀수 노드 : 노드 번호가 홀수 + 자식 노드의 개수가 짝수
            - 역짝수 노드 : 노드 번호가 짝수 + 자식 노드의 개수가 홀수

        목표 : 각 트리에 대한 루트 노드를 설정했을 때, 홀짝 트리가 될 수 있는 트리 개수와 역홀짝 트리가 될 수 있는 트리 개수 구하기
            - 홀짝 트리 : 홀수 노드 + 짝수 노드로만 구성
            - 역홀짝 트리 : 역홀수 노드 + 역짝수 노드로만 구성

            모든 트리는 (홀짝 트리 / 역홀짝 트리 / 둘 다 / 둘다 안됨) 중 하나가 될 수 있음
            → 모든 노드를 루트 노드로 설정해서 홀짝 트리인지 역홀짝 트리인지 판단해야 할듯

        풀이 :
            모든 노드를 루트 노드로 설정해 보면서 홀짝 트리인지 역홀짝 트리인지 판단하는 알고리즘 구성하면 될 것 같음
            깊이 우선 탐색으로 트리를 탐색하기엔 많은 시간이 걸릴 것 같음
            현재 노드 부터 홀짝 노드인지 아닌지 먼저 판단하고, 깊이 들어가면서 판단하면 될듯
    """

    answer = [0, 0]

    # 그래프에 대한 정보 저장
    graph = {node: [] for node in nodes}
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
    

    # 모든 노드를 루트 노드로 두고 트리 종류 구하기
    def check_tree(node):
        q = deque([node])
        tree = -1

        while q:
            cur_node = q.popleft()
            if tree == -2:
                return
            
            if len(graph[cur_node]) == 0:
                return cur_node % 2
            
            else:
                cnt = 0
                for child in graph[cur_node]:
                    if not visited[child]:
                        cnt += 1
                        visited[child] = True
                        q.append(child)

                cur_tree = (cur_node % 2) == (cnt % 2)
                cur_tree = 0 if cur_tree else 1

                if   tree == -1: tree = cur_tree
                elif tree != cur_tree: tree = -2

        return tree                


    for node in nodes:
        visited = [False] * (max(nodes) + 1)
        visited[node] = True
        tree = check_tree(node)
        if tree == 0 or tree == 1:
            answer[tree] += 1

    return answer


def main():
    print(solution([11, 9, 3, 2, 4, 6], [[9, 11], [2, 3], [6, 3], [3, 4]]))
    print(solution([9, 15, 14, 7, 6, 1, 2, 4, 5, 11, 8, 10], [[5, 14], [1, 4], [9, 11], [2, 15], [2, 5], [9, 7], [8, 1], [6, 4]]))


if __name__ == "__main__":
    main()

