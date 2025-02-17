import sys
input = sys.stdin.readline
#queue 자료구조를 사용하기 위한 deque import
from collections import deque
#테스트 케이스 T
T = int(input())
#방향 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
#테스트 케이스마다 배추가 모여있는 구역(필요한 지렁이의 마리 수)을 저장하는 리스트 cnt
cnt = []
#땅에서 배추가 있는 구역들을 찾는 함수 find_baechu() --> BFS
def find_baechu(x, y):
    #Q를 queue자료구조로 만들고
    #배추가 심어져 있는 좌표를 Q에 넣고, 선입선출 방식으로 처리함.
    Q = deque()
    Q.append((x, y))
    #다른 구역으로부터 재탐색 하지 않기 위해 0으로 바꿔주며 방문처리.
    board[x][y] = 0
    #Q가 채워져 있다면 배추가 있는 것이므로 while로 더이상 배추가 안나올때까지 탐색.
    while Q:
        # popleft() : queue의 선입선출 즉, queue자료구조에서 가장 왼쪽(가장 먼저 들어간)에 있는 것을 빼는 내장함수.
        temp = Q.popleft()
        # 배추가 심어진 곳 상, 하, 좌, 우 네 방향을 탐색
        for i in range(4):
            #nx, ny는 next x, next y라고 보면 됨.
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            #nx, ny가 땅 범위에서 벗어나지 않고 해당 좌표에 배추가 심어져 있다면,
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:
                #방문처리 및 Q에 넣어주기.
                board[nx][ny] = 0
                Q.append((nx, ny))
    
for _ in range(T):
    #각 테스트 케이스에서 필요한 지렁이의 수 cnt_jirung
    cnt_jirung = 0
    #문제에서 설정하는 M, N, K
    M ,N, K = map(int, input().split())
    #땅을 나타내는 board
    board = [[0] * M for _ in range(N)]
    #(a, b) 위치에 배추가 심어짐
    for i in range(K):
        a, b = map(int, input().split())
        board[b][a] = 1
    #모든 땅을 탐색
    for j in range(N):
        for k in range(M):
            #탐색 하며 배추가 있으면 근처 배추가 있는 구역을 너비탐색
            if board[j][k] == 1:
                find_baechu(j, k)
                #배추가 있는 구역 cnt_jirung을 한 개 올려줌.
                cnt_jirung += 1

    cnt.append(cnt_jirung)
#모든 테스트 케이스에 대해 배추를 카운트 한 것을 저장한 cnt리스트 출력.
for x in cnt:
    print(x)
