import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

"""
    처음 풀이인데, 1%도 안가서 틀렸다고 나옴..
    1. 집과 치킨집에 대한 정보 저장
    2. 집과 치킨집이 어떻게 링크되는지 정보 저장
    3. 가장 링크가 많이 되는 치킨집부터 남기기
    4. 만약 동일하게 링크가 된다면, 모든 집들의 평균 위치와 가장 근접한 치킨집을 남기기

    이런 반례가 있기 때문
    5 2
    1 1 2 0 2
    2 1 1 2 2
    0 0 2 1 0
    2 0 1 1 0
    0 1 0 2 1
    Correct : 14
    Wrong : 24


    다시 돌아가서 → 조합으로 문제 푸는 것이 정석
    치킨집에 대한 정보를 저장한 뒤, m개의 치킨집을 선택해 최솟값이 되는 거리를 구하는 방법으로 접근
    - 코드 참고 : https://crush-on-study.tistory.com/254
    
"""

def calculate_distance(house, chick):
    return abs(house[0] - chick[0]) + abs(house[1] - chick[1])

# 집과 치킨집 정보 저장
house_info = []
chick_info = []
for y in range(n):
    for x in range(n):
        if   arr[y][x] == 1: house_info.append((y, x))
        elif arr[y][x] == 2: chick_info.append((y, x))


visited_chick = []
result = sys.maxsize

def combination(num, count):
    global result

    if len(chick_info) < num:
        return
    
    if count == m:
        chick_dist = 0
        for house in house_info:
            min_dist = sys.maxsize
            for idx in visited_chick:
                min_dist = min(min_dist, calculate_distance(house, chick_info[idx]))
            chick_dist += min_dist
        result = min(result, chick_dist)
        return
    
    visited_chick.append(num)
    combination(num + 1, count + 1)
    visited_chick.pop()
    combination(num + 1, count)

combination(0, 0)
print(result)

