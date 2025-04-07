import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    스패닝 트리란, 그래프의 최소 연결 부분 그래프
    즉, n개의 정점을 가지고 있는 트리라면 n-1개의 간선으로 연결된 트리

    최소 신장/스패닝 트리 (Minimum Spanning Tree)란,
    스패닝 트리 중, 간선의 가중치가 최소가 되는 트리 
"""

"""
    크루스칼 (Kruskal) 알고리즘으로 최소 비용 신장 트리 만들기
    1. 모든 간선을 가중치가 작은 순으로 오름차순 정렬
    2. 정렬된 간선 리스트 중 가장 작은 가중치를 가진 간선 선택
    3. 사이클 체크 - 해당 간선을 추가했을 때, 트리 내 사이클 발생하는지 확인 (Union-Find)
    4. 트리 구성 - 사이클이 발생하지 않은 간선만 트리에 추가
"""

def find(parents, x):

    # 자기 자신이 트리 시작점이 아니라면,
    # 내 노드와 연결된 상위 노드를 타고 들어가기
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]


def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)

    # a와 b 노드의 트리 시작점 (부모 노드)가 다르다면,
    # b노드를 a에 연결하고 union = True 출력
    if a != b:
        parents[b] = a
        return True
    return False


while True:
    m, n = map(int, input().split())
    if (m, n) == (0, 0):    # 마지막 테스트인 경우 종료
        break
    
    # 간선의 가중치가 작은 순으로 오름차순 정렬
    edges = [list(map(int, input().split())) for _ in range(n)]
    edges.sort(key=lambda x: x[-1])

    # 가중치가 가장 작은 간선을 선택해 트리 구성했을 때 사이클 발생하는지 확인
    parents = [i for i in range(m)]
    cost = 0
    for x, y, z in edges:
        if not union(parents, x, y):
            cost += z

    print(cost)