import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
times = sorted(list(map(int, input().split())))

"""
    일단 시간이 가장 적게 걸리는 사람 순으로 정렬하면
    각 사람이 돈을 인출하는데 걸리는 시간이 적게 걸림
"""

result = 0
for i in range(1, len(times) + 1):
    result += sum(times[:i])
print(result)