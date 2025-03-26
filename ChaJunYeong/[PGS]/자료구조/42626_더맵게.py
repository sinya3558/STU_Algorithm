"""
    모든 음식의 스코빌 지수를 K 이상으로 만들기
    스코빌 지수가 가장 낮은 두개의 음식을 특별한 방법으로 섞어 새로운 음식 만들기
    
    * 섞은 음식의 스코빌 = 가장 맵지 않은 음식의 스코빌 + (두번째로 맵지 않은 음식의 스코빌 * 2)

    모든 음식의 스코빌 지수가 K 이상이 될 때 까지 반복해서 섞기
    섞어야 하는 최소 횟수 return


    풀이 : 
        우선순위 큐로 문제 풀기
        - 입력 받은 리스트를 최소 힙으로 변환
        - 최소 힙에서 가장 스코빌 지수가 낮은 음식부터 꺼내오기
        
        # 이때, 남아있는 음식이 1개 이면서, 스코빌 지수가 목표로 하는 수치보다 낮다면 -1, 그렇지 않으면 섞은 횟수 return
        # 가장 맵지 않은 음식 꺼내올 때, 
        #   스코빌 지수가 목표로 하는 수치보다 낮다면 섞은 횟수 return
        #   그렇지 않으면 음식섞고 반복
"""

def solution(scoville, K):

    import heapq
    answer = 0
    heapq.heapify(scoville)

    while True:

        # 남아있는 음식이 1개일 경우, 
        if len(scoville) == 1:
            return answer if K <= scoville[0] else -1
        
        # 남아있는 음식이 2개 이상일 경우, 음식 섞기
        #   1. 이때 가장 맵지 않은 음식이 K보다 클 경우, 섞을 필요 없음
        #   2. 그렇지 않을 경우, 음식 섞기

        first  = heapq.heappop(scoville)
        if K <= first: return answer

        second = heapq.heappop(scoville)
        mix = first + second * 2

        answer += 1
        heapq.heappush(scoville, mix)



def main():
    print(solution([1, 2, 3, 9, 10, 12], 7))
    print(solution([3, 2, 1, 9, 10, 12], 7))


if __name__ == "__main__":
    main()