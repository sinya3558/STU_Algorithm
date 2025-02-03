import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

# 종료 시간 기준으로 오름차순 정렬
arr = sorted(arr, key=lambda x: x[1])

# 일찍 끝나는 순서부터 차례대로 회의실 배정
# 1. 맨 처음 회의를 회의실에 배정
# 2. 이전 회의가 끝나는 시간과 다음 회의 시작 시간 비교
cnt = 0
last_e = -1
for s, e in arr:
    if last_e <= s:
        cnt += 1
        last_e = e

print(cnt)
