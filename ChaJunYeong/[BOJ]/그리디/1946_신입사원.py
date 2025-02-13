import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    목표 : 이번 신규 사원 채용에서 선발 가능한 최대 인원 수
    조건 : 
        - 서류심사 + 면접시험 중 적어도 하나가 다른 지원자보다 떨어지지 않은 사람만 선발
        - 즉, 모든 심사 성적이 다른 지원자보다 떨어질 경우 탈락
"""

def test_case(applicants):
    a = sorted(applicants, key=lambda x: x[0])
    
    # 일단 서류 심사의 성적이 제일 좋은 사람부터 뽑음
    # 이전 면접 시험의 성적이 제일 좋았던 사람보다 성적이 좋을 경우 뽑음

    cnt = 1
    min_document, min_interview = a[0]
    for document, interview in a[1:]:
        if interview < min_interview:
            cnt += 1
            min_interview = interview
    return cnt

T = int(input())
for _ in range(T):
    n = int(input())

    applicants = list()
    for i in range(n):
        applicants.append(tuple(map(int, input().split())))
    print(test_case(applicants))
