from collections import deque

def solution(storage, requests):
    
    """
        특정 종류 컨테이너 출고 요청이 들어올 때마다 지게차로 창고에서 접근이 가능한 해당 종류의 컨테이너 모두 꺼냄
        여기서 접근이 가능한이란 → 4면 중 적어도 1면이 외부와 연결된 컨테이너
        외부와 연결되어 있지 않아도 꺼낼 수 있도록 크레인 도입 (크레인을 사용하면 요청된 모든 컨테이너 꺼낼 수 있음)

        조건 1 : 요청이 들어온 컨테이너가 알파벳 하나로 들어오면 지게차로 꺼냄 (ex. 'A')
        조건 2 : 요청이 들어온 컨테이너가 같은 알파벳이 두번 반복되면 크레인으로 꺼냄 (ex. 'BB')

        목표 : 모든 요청을 처리했을 때 남아있는 컨테이너의 갯수 출력

        풀이 : 
            컨테이너가 외부 인지, 내부인지 판단하는 것이 중요한 듯
            0. 외부와 내부를 판단하는 컨테이너 배열 / 출고된 컨테이너인지 아닌지 판단하는 배열 초기화
                1. 외부는 1 / 내부는 0으로 초기화
                2. 컨테이너가 출고되었으면 0 / 출고되지 않았으면 1로 초기화

            1. 지게차 혹은 크레인으로 출고
                1-1. 지게차로 출고할 경우, 해당 컨테이너가 외부이면서 한 번도 출고되지 않았어야 함
                1-2. 크레인으로 출고할 경우, 한 번도 출고되지 않았어야 함

            2. 내부가 아닌 어떤 컨테이너를 출고했을 경우,
                2-1. 해당 컨테이너와 연결된 다른 컨테이너가 출고되지 않았다면 외부로 초기화
                2-2. 만약 연결된 컨테이너가 출고되었는데 내부로 판단된다면, 그와 연결된 다른 컨테이너를 외부로 초기화
    """

    h, w = len(storage), len(storage[0])
    out_side = [[1] * w for _ in range(h)]  # 외부이면 1, 내부면 0으로 초기화
    for i in range(1, h-1):
        out_side[i][1:w-1] = [0] * (w - 2)
    not_used = [[1] * w for _ in range(h)]  # 출고 전이면 1, 출고 후는 0으로 초기화

    # 요청을 하나씩 처리
    for req in requests:
        req_container = req[0]
        used_lst = deque()

        # 1-1. 지게차로 출고할 경우, 출고되지 않았으면서 반드시 외부여야 함
        if len(req) == 1:
            for y in range(h):
                for x in range(w):
                    if storage[y][x] == req_container and not_used[y][x] and out_side[y][x]:
                        not_used[y][x] = 0
                        used_lst.append((y, x))

        # 1-2. 크레인으로 출고할 경우, 출고되지만 않았으면 됨
        elif len(req) == 2:
            for y in range(h):
                for x in range(w):
                    if storage[y][x] == req_container and not_used[y][x]:
                        not_used[y][x] = 0
                        if out_side[y][x]: used_lst.append((y, x))

        # 2. 컨테이너를 출고하고 난 후, 외부와 내부 다시 구분해주기
        # 내부가 아닌 어떤 컨테이너를 출고했을 때, 4 방향을 돌면서 외부인지 내부인지 확인
            # 2-1. 출고된 컨테이너와 연결된 컨테이너가 출고되지 않은 경우 외부로 초기화
            # 2-2. 연결된 컨테이너가 출고된 후임에도 내부로 판단되는 경우에는, 그와 연결된 컨테이너를 외부로 초기화
        while used_lst:
            y, x = used_lst.popleft()
            for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                ny, nx = dy + y, dx + x
                if 0 <= ny < h and 0 <= nx < w:
                    if not_used[ny][nx]:
                        out_side[ny][nx] = 1
                    elif not not_used[ny][nx] and not out_side[ny][nx]:
                        out_side[ny][nx] = 1
                        used_lst.append((ny, nx))

    answer = sum([sum(not_used[i][:]) for i in range(h)])
    return answer



def main():
    print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]))
    print(solution(["HAH", "HBH", "HHH", "HAH", "HBH"], ["C", "B", "B", "B", "B", "H"]))
    print(solution(["AAAA", "ABAA", "ABAA", "ACAA", "AAAA"], ["BB","C"]))
    


if __name__ == "__main__":
    main()
