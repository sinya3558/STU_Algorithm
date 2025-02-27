from collections import deque

def solution(maps):

    """
        00:13:24.78
        
        게임 내에서 상대 진영에 도착하기 위해 지나야 하는 칸의 갯수의 최솟값
        조건 : (1, 1)에서 출발 (n, m)에 도착

        풀이 : 
            너비 우선 탐색 (BFS)로 풀이
            1. 로봇이 해당 위치에서 움직일 수 있는 공간 찾기
                1-1. 범위를 벗어나면 안됨 (인덱스를 벗어나면 안됨)
                1-2. 벽에 가로막히면 안됨
                1-3. 한 번 방문했던 곳은 재방문 할 수 없음
            2. 만약 이동할 수 있다면, 이동한 위치의 좌표와, 해당 칸으로 이동하기 위해 지나야했던 칸 수 저장
    """

    n = len(maps)
    m = len(maps[0])
    visited = [[n * m + 1] * m for _ in range(n)]
    visited[0][0] = 1
    q = deque([(0, 0, 1)])

    while q:
        cur_y, cur_x, cur_cnt = q.popleft()

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ny, nx = cur_y + dy, cur_x + dx

            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1 and visited[ny][nx] == (n * m + 1):
                visited[ny][nx] = min(visited[ny][nx], cur_cnt + 1)
                q.append((ny, nx, cur_cnt + 1))
                
    return visited[n-1][m-1] if visited[n-1][m-1] != (n * m) + 1 else -1


def main():

    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
    print(solution([[1, 1, 1, 1, 1]]))


if __name__ == "__main__":
    main()
