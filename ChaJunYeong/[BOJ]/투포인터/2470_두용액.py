import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
arr = sorted(list(map(int, input().split())))

# 왼쪽 끝 포인터, l
# 오른쪽 끝 포인터, r

# 1. 두 포인터의 합이 이전 포인터들의 합보다 작으면, 정답 값 초기화 → 이후 최솟값 계속 탐색
# 2. 두 포인터의 합이 0보다 작으면, l += 1
# 3. 두 포인터의 합이 0보다 크면, r -= 1
# 4. 두 포인터의 합이 0이면 break
# 이때, l >= r이면 break

l, r = 0, n-1
min_mix = sys.maxsize
result = [arr[l], arr[r]]

while l < r:
    mix = arr[l] + arr[r]

    # 1.
    if abs(mix) < min_mix:
        min_mix = abs(mix)
        result = [arr[l], arr[r]]

    # 2.
    if mix < 0:
        l += 1

    # 3.
    elif 0 < mix:
        r -= 1

    # 4.
    else:
        break

print(result[0], result[1])