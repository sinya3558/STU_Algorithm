def solution(begin, target, words):

    """
        00:14:02.94
        
        begin -> target 으로 변환하는 가장 짧은 변환 과정 찾기
        조건 1 : 한 번에 한 개의 알파벳만 바꿀 수 있음
        조건 2 : words에 있는 단어로만 바꿀 수 있음

        풀이 : 
            깊이 우선 탐색 (BFS)로 풀이
            1. words에 있는 단어로 순열 만들기
            2. 순열을 만들다가,
                2-1. 이전 단어와 한글자 차이가 나는 경우
                2-2. 이전에 한 번도 방문한 적이 없는 경우
                해당 단어로 변환.
                그렇지 않으면 순열 빠져나오기
            3. target이 완성되면 최솟값 구하기
    """

    answer = len(words) + 1
    visited = [False] * len(words)

    def dfs(depth, cur_word):
        nonlocal answer

        if cur_word == target:
            answer = min(answer, depth)
            return
        
        else:
            for i in range(len(words)):
                next_word = words[i]

                if not visited[i]:
                    cnt = 0
                    for cur_ch, next_ch in zip(cur_word, next_word):
                        if cur_ch != next_ch:
                            cnt += 1
                    
                    if cnt != 1:
                        continue
                    
                    visited[i] = True
                    dfs(depth + 1, next_word)
                    visited[i] = False

    dfs(0, begin)
    return answer if answer != len(words) + 1 else 0



# from collections import deque
# def solution(begin, target, words):
#     # 너비 우선 탐색 (BFS)로도 풀이가 가능

#     answer = len(words) + 1
#     q = deque([(begin, 0)])
#     visited = [False] * len(words)

#     while q:
#         cur_word, cur_cnt = q.popleft()
#         if cur_word == target:
#             answer = min(answer, cur_cnt)

#         for i in range(len(words)):
#             next_word = words[i]

#             if not visited[i]:
#                 cnt = 0
#                 for cur_ch, next_ch in zip(cur_word, next_word):
#                     if cur_ch != next_ch:
#                         cnt += 1

#                 if cnt == 1:
#                     visited[i] = True
#                     q.append((next_word, cur_cnt + 1))

#     return answer if answer != len(words) + 1 else 0
    


def main():
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))


if __name__ == "__main__":
    main()

