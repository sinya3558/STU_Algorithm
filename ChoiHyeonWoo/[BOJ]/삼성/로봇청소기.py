#N,M : 격자의 크기
N,M = map(int,input().split())
# r,c 로봇 청소기 좌표
r,c,d = map(int, input().split())
#격자 입력
graph = [list(map(int, input().split())) for _ in range(N)]
#방향 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# answer == 청소한 칸의 갯수
answer = 0
# 후진했을 때 벽이면 end를 1로 변경하기 위한 변수 선언
end = 0
#계속해서 청소
while 1:
    #cnt는 동서남북 중 벽이나 청소한 칸의 개수
    cnt = 0
    # 로봇 청소기 좌표의 격자가 0 이면 청소했단 의미로 2로 변경, 청소한 칸 +1 추가
    if graph[r][c] == 0:
        graph[r][c] = 2
        answer+=1
    #동서남북 체크
    for i in range(4):
        #nx, ny는 북-동-남-서 방향으로 돌아감
        nx = r + dx[i]
        ny = c + dy[i]
        # nx, ny가 격자 범위 안이라면
        if 0 <= nx < M and 0 <= ny < N:
            #만약 로봇청소기 기준 북동남서 중 0인 칸이 있다면
            if graph[nx][ny] == 0:
                #d(방향) 90도 반시계 방향 회전
                d -= 1
                #d가 음수가 되면 3으로 변경
                if d < 0:
                    d = 3
                #nx,ny = 바라보고 있는 좌표
                nx = r + dx[d]
                ny = c + dy[d]
                #바라보고 있는 좌표가 격자범위 안이면
                if 0 <= nx < M and 0 <= ny < N:
                    #바라보고 있는 좌표에 있는값이 0(청소안한 빈칸)이라면
                    if graph[nx][ny] == 0:
                        #해당 칸으로 전진하기 위해 로봇청소기 좌표 변경
                        r, c = nx, ny
                        #동서남북 체크 반복문 종료
                        break
            #동서남북 체크할 때 1보다 크면(1은 벽, 2는 청소한 칸) cnt 1 증가
            elif graph[nx][ny] >= 1:
                cnt += 1
            #만약 cnt가 4로 주위에 청소되지 않은 빈칸이 없다면(조건 2번)
            if cnt == 4:
                #후진하기 위한 nx, ny 설정
                #d(바라보는 방향)이 2보다 크거나 같으면 방향 리스트 에서 -2로
                # 좌표 후진 설정
                if d >= 2:
                    nx = r + dx[d-2]
                    ny = c + dy[d-2]
                #d(바라보는 방향)이 2보다 작으 방향 리스트 에서 +2로 좌표 후진 설정
                elif d < 2:
                    nx = r + dx[d+2]
                    ny = c + dy[d+2]
                #후진 된 좌표로 로봇 청소기 좌표 설정
                r,c = nx, ny
                #후진 된 좌표로 이동했을 때 1(벽)이면 while문 종료하기 위한 end+=1
                if graph[r][c] == 1:
                    end = 1
    #end가 1이 되면 while문 종료
    if end == 1:
        break
#청소한 칸 출력
print(answer)




