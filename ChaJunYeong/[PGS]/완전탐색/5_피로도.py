def solution(k, dungeons):

    """
        00:25:18.70

        각 던전별로 탐험할 때 필요한 "최소 필요 피로도"와 던전 탐험 시 소모되는 "소모 피로도" 존재
        각각을 x, y라고 지칭하면, x = 80, y = 20인 던전을 돌기위해서
        유저의 남은 피로도는 80 이상이어야 하며, 던전 탐험 후 피로도 20이 소모됨
        유저의 피로도와 각 던전의 피로도 정보가 주어졌을 때, 유저가 돌 수 있는 최대 던전의 수 구하기

        갚이 우선 탐색으로 진행
        1. 피로도와 깊이에 대한 정보 전달
        2. 만약, 깊이가 최대 길이에 도달할 경우 break
        3. 그렇지 않을 경우, 이전에 방문하지 않았던 다음 던전 탐색
            3-1. 현재 남은 스테미나가 최소 필요 피로도보다 높아야함
            ※ 소모 피로도는 항상 최소 필요 피로도보다 작으므로 고려하지 않아도 됨
            
    """

    answer = -1
    is_visited = [False] * len(dungeons)
    def dfs(stemina, depth):
        nonlocal answer
        
        # 만약 방문할 수 있는 모든 던전을 다 돌았으면, answer 값 업데이트
        if depth == len(dungeons):
            answer = max(answer, depth)
            return
        
        # 추가로 방문할 수 있는 던전 있는지 확인하기
        # 조건 1. 이전에 방문하지 않았던 던전 중에서
        # 조건 2. 던전 탐험에 필요한 스테미너가 현재 남은 스테미너보다 작은 경우
        else:
            for i in range(len(dungeons)):
                need_stemina, used_stemina = dungeons[i]
                if not is_visited[i]:

                    # 만약 현재 남은 스테미너로 해당 던전을 돌지 못할 경우, 그 다음 던전 탐색색                    
                    if stemina < need_stemina:
                        answer = max(answer, depth)
                        continue
                    
                    is_visited[i] = True
                    dfs(stemina - used_stemina, depth + 1)
                    is_visited[i] = False

    # 깊이 우선 탐색으로 진행행
    dfs(k, 0)
    return answer


def main():
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))


if __name__ == "__main__":
    main()