import sys
def input():
    return sys.stdin.readline().rstrip()

x = list(input())

""" 기존 풀이
    순서가 상관있는 오리 울음소리 ㅡ 예를 들어서, q가 나오기 전에 u가 나올 순 없음

    1. q, u, a, c, k 각각의 index를 1, 2, 3, 4, 5라고 지정
    2. q에 대해서
        2-1. q, u, a, c, k를 한바퀴 다 돈 상태에서 넣을 수 있음
        2-2. 새로운 오리가 출현할 수도 있음
    3. u에 대해서
        3-1. q가 나온 이후에만 나올 수 있음
        3-2. 올바르지 않은 울음소리면 바로 빠져나오기
    ...
    4. 울다만 소리가 있는지 먼저 확인
    5. 있으면 -1, 없으면 오리 수 확인

    ★★★ 87%에서 에러발생...
"""


"""
    코드 참고 : https://velog.io/@gilyeon00/%EB%B0%B1%EC%A4%80-12933%EB%B2%88-%EC%98%A4%EB%A6%AC-python-%EC%8B%A4%EB%B2%843
"""

# 우선 올바른 울음소리인지 먼저 체크 (q가 맨 앞, k가 맨 뒤, 울음소리의 길이는 5의 배수여야 함)
if not (x[0] == 'q' and x[-1] == 'k' and len(x) % 5 == 0):
    print(-1)

else:
    def find_quack(start):
        quack = 'quack'
        j = 0
        new_ori = True

        ans = 0
        for i in range(start, len(x)):
            if x[i] == quack[j]:
                if x[i] == 'k':
                    if new_ori:
                        ans += 1
                        new_ori = False
                j = (j + 1) % 5
                x[i] = 0
        return ans

    result = 0
    # q로 시작하는 울음소리가 있다면, 올바른 울음소리인지 체크!
    for i in range(len(x) - 4):
        if x[i] == 'q':
            result += find_quack(i)

    if any(x) or result == 0:
        print(-1)
    else:
        print(result)