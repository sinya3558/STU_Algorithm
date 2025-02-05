import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    순열 조합으로 문제 풀기
    1. 가능한 순열 조합 생성하기
    2. 생성된 순열 조합이 문제 조건의 부등호를 만족하는지 확인
    3. 만족한다면, 최대 / 최솟값 업데이트
    → 시간이 오래 걸리는 코드
    → 모든 순열 조합을 항상 확인하는 것이 아니라, 순열이 만들어지는 depth 단계별로 항상 조건을 만족하는지 확인하면 시간이 절약될 것으로 보임

    n = int(input())
    comp = list(input().split())

    def check_validitiy(comp, i):
        for idx, operator in enumerate(comp):
            val1 = int(i[idx])
            val2 = int(i[idx + 1])

            if operator == "<" and val1 > val2:
                return False
            elif operator == ">" and val1 < val2:
                return False
        return True
                
    max_result = -1
    min_result = sys.maxsize

    from itertools import permutations
    for i in permutations([str(i) for i in range(0, 10)], n + 1): 
        if check_validitiy(comp, i):
            if int(max_result) < int(''.join(i)):
                max_result = ''.join(i)
            if int(min_result) > int(''.join(i)):
                min_result = ''.join(i)

    print(max_result)
    print(min_result)
"""


n = int(input())
comp = list(input().split())

isVisited = [False] * 10
result = []

def check(val1, val2, op):
    if op == "<" and val1 > val2: return False
    if op == ">" and val1 < val2: return False
    return True


def permutation(num, depth):
    if depth == n + 1:
        result.append(num)
        return
    
    for i in range(10):
        if not isVisited[i] and (depth==0 or check(num[-1], str(i), comp[depth-1])):
            isVisited[i] = True
            permutation(num + str(i), depth + 1)
            isVisited[i] = False

permutation('', 0)
sorted(result)
print(result[-1])
print(result[0])    
