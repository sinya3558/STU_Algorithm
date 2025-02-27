def solution(tickets):

    """
        00:40:12.60

        항공권 정보가 주어졌을 때, 방문하는 공항 경로를 출력

        조건 1 : 주어진 항공권은 모두 사용해야 함
        조건 2 : 가능한 경로가 2개 이상일 경우, 알파벳 순서가 앞서는 경로를 return
        조건 3 : 항상 ICN 공항에서 출발
        조건 4 : 이미 방문했던 공항으로 다시 되돌아 올 수 있음

        풀이 : 
            깊이 우선 탐색 (DFS)로 탐색
            1. 모든 티켓을 다 사용한 경우, 해당 공항까지의 경로를 route에 담기
            2. 그렇지 않은 경우 다른 티켓 사용
                2-1. 현재 공항에서 출발하는지
                2-2. 해당 티켓을 한번도 사용하지 않았는지 확인
                조건을 만족하면, 해당 티켓을 사용하여 DFS 탐색
            3. 완전탐색 후, 정렬
            4. 정답 출력

            1번 테스트케이스에서 390.88ms 시간이 걸림 → 어떻게 하면 시간 더 줄일 수 있을까?

    """

    used = [False] * len(tickets)
    route = []

    def dfs(depth, pos):
        if depth == len(tickets):
            route.append(pos)
            return
        
        else:
            cur_pos = pos[-3:]
            for i in range(len(tickets)):
                next_s, next_e = tickets[i]
                if next_s == cur_pos and not used[i]:
                    used[i] = True
                    dfs(depth + 1, pos + next_e)
                    used[i] = False

    dfs(0, 'ICN')
    route.sort()
    return [route[0][i:i+3] for i in range(0, len(route[0]), 3)]


def main():
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))


if __name__ == "__main__":
    main()