import sys
def input():
    return sys.stdin.readline().rstrip()


"""
    풀이 참고 : 
    - https://osnim.tistory.com/entry/%EC%B5%9C%EC%9E%A5-%EA%B3%B5%ED%86%B5-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4-LCSLongest-Common-Subsequence-%ED%8C%8C%EC%9D%B4%EC%8D%AC
    - https://10000cow.tistory.com/entry/%ED%95%9C-%EC%82%B4%EB%8F%84-%EC%9D%B4%ED%95%B4%ED%95%98%EB%8A%94-%EB%B0%B1%EC%A4%80-9251%EB%B2%88-LCS-DPPython

    LCS : Longest Common Subsequence
    두 문자열 사이의 최장 공통 부분 집합을 구하는 문제 (단, 순서는 바뀌면 안됨)
    문제의 조건 : 두 문자열이 공통적으로 반복되는 부분 집합의 최장 길이를 찾는 것
    
    - Top-down 방식의 풀이 : 
        1. 두 부분 집합의 마지막 문자를 비교했을 때 동일하다면 
            두 부분 집합을 하나씩 줄여서 또 비교한 결과에 + 1 
        2. 두 부분 집합의 마지막 문자가 동일하지 않다면, 
            2-1. a 문자열을 하나 줄여서 비교
            2-2. b 문자열을 하나 줄여서 비교
            1과 2의 LCS 중 최댓값을 선택

    Pseudo Code:
    LCS(X, Y):
        m, n = len(X), len(Y)
        if m == 0 or n == 0: return 0
        else:
            if X[-1] == Y[-1]:
                return LCS(X[:m-1], Y[:n-1]) + 1    # 1.
            else:
                return max(
                    LCS(X, Y[n-1]), # 2-1
                    LCS(Y, X[m-1])  # 2-2
                )

    → 이 방법으로 풀이할 경우, 결국 중복되는 부분이 발생할 수 있음
    → Top-down 방식으로, 재귀적으로 문제를 풀이할 경우 O(2^n)의 시간 복잡도를 가지게 됨

    ─────────────────────────────────────────────────────────────────────────
    
    - bottom-up 방식의 풀이 : (DP Table에 이미 계산한 값을 저장)
        1. 두 부분 집합의 문자열을 비교했을 때, 동일하다면 DP table의 왼쪽 대각선에 + 1
        2. 동일하지 않다면, 왼쪽 혹은 위쪽 값중 큰 값을 저장
    
    ※ DP table을 2차원으로 구성했을 때, 두 부분 집합의 마지막 문자가 동일하다면 왼쪽 대각선 LCS에 +1을 해주어야 하는가?
        - 이는 앞서 Top-down 방식의 1번 조건을 참고하면 됨.
            결국, 두 부분 집합의 문자가 동일하여 LCS가 하나 증가하는 상황이면, 각 부분집합의 문자를 하나씩 줄였을 때의 LCS에 +1 한 값과 동일하기 때문
            그렇지 않다면, 두 부분 집합의 문자열을 각각 하나씩 줄였을 때의 최댓값을 LCS라고 생각하는 것도 마찬가지의 이유 (2번 조건에 의헤)

    Pseudo Code:
        LCS(X, Y):
            X, Y = " "+X, " "+Y
            for i in range(1, len(X) = 1):
                for j in range(1, len(Y) - 1):
                    if X[i] == Y[j]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(
                        dp[i-1][j], 
                        dp[i][j-1]
                    )

    ex) a = ACAYKP, b = CAPCAK 라고 한다면,
        -    C   A   P   C   A   K
    -   0   0   0   0   0   0   0
    A   0   0   1   1   1   1   1
    C   0   1   1   1   2   2   2
    A   0   1   2   2   2   3   3
    Y   0   1   2   2   2   3   3
    K   0   1   2   2   2   3   4
    P   0   1   2   3   3   3   4

    최종적으로 LCS는 DP talbe의 우 하단값 (두 문자열을 모두 돌았을 때의 결과)과 동일함
"""

a = input()
b = input()

dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])