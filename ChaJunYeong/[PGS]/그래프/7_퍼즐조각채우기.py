from collections import deque
def solution(game_board, table):

    """
        02:27:06.48

        테이블 위에 놓여진 퍼즐 조각을 게임 보드 빈 공간에 채우기
        조건 1 : 조각은 한 번에 하나씩 채우기
        조건 2 : 회전 가능 / flip 불가능
        조건 3 : 조각을 채워넣었을 때, 인접한 칸이 비어 있으면 안됨 (딱 들어맞게 넣어야 함)

        풀이 : 
            너비 우선 탐색 (BFS)로 풀이
            1. 게임 보드 내 빈 공간에 대한 정보를 BFS 로 탐색한 후 저장
            2. Table 위의 게임 조각들에대한 정보 역시 BFS로 탐색
                2-1. 게임 보드 내 빈 공간이 한 번도 사용된 적 없고
                2-2. 빈공간의 개수와 게임 조각의 갯수가 같으면
                해당 게임 조각을 빈 공간에 채우기 (갯수 업데이트)
                
        풀이의 접근 방식은 맞는 것 같은데, 확신이 없음
        특히, 조각의 회전 부분 구현 못함
        빡구현 문제

        ※ 풀이 참고

    """

    # 조각 찾기 알고리즘 (너비 우선 탐색)
    def find_piece(board, flag):
        pieces = []
        visited = [[False] * len(board[0]) for _ in range(len(board))]

        for y in range(len(board)):
            for x in range(len(board[0])):
                
                # 방문하지 않았던 위치에 조각이 있는 경우, 해당 좌표와 연결된 모든 좌표를 찾아 조각으로 연결
                if not visited[y][x] and board[y][x] == flag:
                    q = deque([(y, x)])
                    visited[y][x] = True
                    lst = [(y, x)]

                    while q:
                        cy, cx = q.popleft()
                        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                            ny, nx = cy + dy, cx + dx

                            # 1. 인덱스 내부에 있어야 함
                            # 2. 조각 좌표여야 함
                            # 3. 한번도 방문하지 않았어야 함
                            if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and not visited[ny][nx] and board[ny][nx] == flag:
                                q.append((ny, nx))
                                visited[ny][nx] = True
                                lst.append((ny, nx))
                    pieces.append(lst)
        return pieces
    

    # 2차원 배열 형태로 만들기
    def make_table(positions):
        y, x = zip(*positions)
        h, w = max(y) - min(y) + 1, max(x) - min(x) + 1

        arr = [[0] * w for _ in range(h)]
        for cy, cx in positions:
            arr[cy-min(y)][cx-min(x)] = 1
        return arr
    
    
    # 시계 방향으로 90도 회전
    def rotation(arr):
        rotated_arr = [[0] * len(arr) for _ in range(len(arr[0]))]  # 가로와 세로 길이가 반전되어야 함

        for y in range(len(arr)):
            for x in range(len(arr[0])):
                rotated_arr[x][len(arr) - 1 - y] = arr[y][x]
        return rotated_arr
        

    
    # 1. 게임 보드 내 빈 공간 찾기
    empty_pieces = find_piece(game_board, 0)

    # 2. 테이블 위 퍼즐 조각 찾기
    puzzles = find_piece(table, 1)

    # 3. 퍼즐 조각을 게임 보드에 넣어보기
    answer = 0
    used = [False] * len(empty_pieces)
    for puzzle in puzzles:
        filled = False
        puzzle_arr = make_table(puzzle)

        for i in range(len(empty_pieces)):
            empty = empty_pieces[i]

            # 빈 조각이 채워졌으면 break
            if filled:
                break

            # 3-1. 퍼즐 조각을 사용하지 않았거나, 퍼즐 조각 좌표 개수와 빈 좌표의 개수가 동일할 때만 비교
            if not used[i] and len(puzzle) == len(empty):
                empty_arr = make_table(empty)

                for _ in range(4):
                    puzzle_arr = rotation(puzzle_arr)
                    if puzzle_arr == empty_arr:
                        used[i] = True
                        filled = True
                        answer += len(puzzle)
                        break

    return answer


def main():
    print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
    print(solution([[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]]))

    
if __name__ == "__main__":
    main()