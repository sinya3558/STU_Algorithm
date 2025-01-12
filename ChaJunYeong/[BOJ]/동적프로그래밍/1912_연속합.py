import sys
def input():
    return sys.stdin.readline().rstrip()

# import sys
# sys.stdin = open('input.txt', 'r')

"""
    동적 프로그래밍 (DP)
    - https://cobi-98.tistory.com/42

    큰 문제를 작은 문제로 나눈 뒤, 기억하여 푸는 기법
    1. Top-down, Memorization : 
        - 중복되는 계산은 한 번만 계산하는 재귀 방식
        - 작은 값부터 캐시에 값을 채워나가는 방식
    2. Bottom-up, Tabulation : 
        - 답을 구하기 위한 모든 계산을 Table 방식으로 저장하는 for문 방식
        - 계산된 값을 캐시에서 꺼내는 방식

    연속 합
    - 코드 참고 : https://data-marketing-bk.tistory.com/entry/%EB%B0%B1%EC%A4%80-1912%EB%B2%88-%EC%97%B0%EC%86%8D%ED%95%A9%ED%8C%8C%EC%9D%B4%EC%8D%AC#google_vignette
    
    연속 된 수들의 합 중 최댓값을 구하는 문제
    - 규칙 :
        - 입력 받은 배열을, 연속 된 수의 합이라고 가정
        - 그렇다면, 현재 아이템과 이전까지의 합이 현재 아이템보다 작을 경우 이전 까지의 합은 의미가 없음
"""

# 입력받기
n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    arr[i] = max(arr[i], arr[i] + arr[i - 1])

print(max(arr))
