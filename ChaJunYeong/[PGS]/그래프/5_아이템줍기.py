from collections import deque

# 직사각형 지도 만들기
def solution(rectangle, characterX, characterY, itemX, itemY):
    
    """
        01:18:22.23

        겹쳐진 직사각형의 제일 바깥쪽 변두리만을 따라서 이동함
        조건 1 : 직사각형의 꼭짓점이 만나거나 변이 겹치는 경우 없음
        조건 2 : 직시각형이 떨어져 있는 경우는 없음
        조건 3 : 한 직사각형이 다른 직사각형 내부에 완전히 포함되는 경우 없음

        cx, cy 위치에서 ix, iy 위치로 이동해야 하는 가장 짧은 거리 return
        
        첫번째 시도 : 
            직사각형 지도 만들고, 캐릭터가 해당 아이템으로 이동하도록 만들기
            → 이때, 직사각형 지도를 만들 때, 테두리로 이동하는 부분에서 반례가 생김
            예를 들어, 
                    1 2 3 4 5
                1   0 0 0 0 0
                2   0 1 1 0 0
                3   0 1 1 0 0
                4   0 1 1 0 0
            위와 같은 지도에서 (3, 2) → (3, 3) 으로 이동하면 안됨
            하지만 이부분 예외 처리를 어떻게 해야 할지 모르겠음

        ※ 풀이 참고
        https://velog.io/@leeeeeyeon/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%95%84%EC%9D%B4%ED%85%9C-%EC%A4%8D%EA%B8%B0

        그렇다면 각각의 좌표를 2배씩 해서 2배로 늘려주면 된다.
        앞선 예시를 예로 들면,
                1 2 3 4 5 6 7 8 9 10
            1   0 0 0 0 0 0 0 0 0 0
            2   0 0 0 0 0 0 0 0 0 0 
            3   0 0 0 0 0 0 0 0 0 0 
            4   0 0 0 1 1 1 0 0 0 0 
            5   0 0 0 1 0 1 0 0 0 0
            6   0 0 0 1 0 1 0 0 0 0
            7   0 0 0 1 0 1 0 0 0 0
            8   0 0 0 1 1 1 0 0 0 0
        이렇게 테두리와 내부를 구분해줄 수 있음
    """
    
    def make_map():
        arr = [[-1] * 102 for _ in range(102)]
        for r in rectangle:
            x1, y1, x2, y2 = map(lambda x: x * 2, r)
            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):

                    # 직사각형의 내부는 0으로 채움
                    if x1 < x < x2 and y1 < y < y2:
                        arr[y][x] = 0

                    # 직사각형의 테두리는 1로 채움
                    elif arr[y][x] != 0:
                        arr[y][x] = 1
        return arr
    

    # 1. 지도 만들기
    maps = make_map()

    # 2. 너비 우선 탐색 (BFS)를 활용해 캐릭터 → 아이템 먹는데 걸리는 최단 시간 구하기
    cx, cy = characterX * 2, characterY * 2
    ix, iy = itemX * 2, itemY * 2
    visited = [[0] * 102 for _ in range(102)]
    q = deque([(cy, cx, 1)])

    answer = -1
    while q:
        cy, cx, cnt = q.popleft()
        if cx == ix and cy == iy:
            if answer == -1: answer = cnt
            else:            answer = min(answer, cnt)

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < 102 and 0 <= nx < 102 and maps[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = 1
                q.append((ny, nx, cnt + 1))

    # 3. 각 좌표를 2배씩 해주었으므로, 경로에 도달할때 까지 걸리는 시간 역시 2배로 늘어남
    answer = answer // 2
    return answer


def main():
    print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
    print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1))
    print(solution([[1,1,5,7]], 1, 1, 4, 7))
    print(solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10))
    print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3))


if __name__ == "__main__":
    main()