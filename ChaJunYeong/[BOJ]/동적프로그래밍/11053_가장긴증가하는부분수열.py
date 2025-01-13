import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    1번째 시도 → 메모리 초과
    2번째 시도 → 시간 초과
    3번째 시도 → 메모리 초과
    DP에 대한 이해가 부족하다고 판단 → 코드 참고하면서 공부
    

    -------------------------------------
    DP 참고 : https://jjuke-brain.tistory.com/entry/Ch05-%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-feat-%EC%9D%B4%EA%B2%83%EC%9D%B4-%EC%B7%A8%EC%97%85%EC%9D%84-%EC%9C%84%ED%95%9C-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4

    # What is DP?
    메모리를 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법
    이미 계산된 결과 (sub problem의 결과)를 별도의 메모리에 저장해두었다가, 필요할 때 다시 계산하지 않고 그대로 사용

    # Condition
    1. 최적의 부분 구조 → 큰 문제를 작은 문제로 나누고, 작은 문제의 답을 모아 큰 문제를 해결
    2. 중복되는 부분 문제 → 부분 문제가 서로 중첩되어 여러번 등장

    # How to Solve DP Problem
    1. Top-down :  
        큰 문제를 해결하기 위해 작은 문제를 재귀적으로 호출, 한번 계산된 결과를 메모리 공간에 메모
    2. Bottom-up : 
        작은 문제를 해결해가면서 먼저 계산했던 문제들의 값을 활용, DP table에 계산된 결과를 저장

        
    -------------------------------------
    코드 참고 : https://it-adventures.tistory.com/109


    현재 아이템과 이전 아이템과 비교
        - 이 때, 현재 아이템이 더 클 경우,
        - 이전 아이템 까지 부분 수열의 최대 길이에 + 1
        - 최댓값을 저장
"""

n = int(input())
arr = list(map(int, input().split()))

length = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]: # 현재 item이 이전 item 보다 클 경우 length update
            length[i] = max(length[i], length[j] + 1)

print(max(length))
