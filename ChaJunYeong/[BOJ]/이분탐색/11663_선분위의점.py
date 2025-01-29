import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
dots = sorted(list(map(int, input().split())))

def binary_search(num, is_start=True):
    l, r = 0, len(dots) - 1

    while l <= r:
        mid = (l + r) // 2
        if num == dots[mid]:
            return mid
        elif num < dots[mid]:
            r = mid - 1
        elif dots[mid] < num:
            l = mid + 1

    if is_start:
        return max(l, r)
    else:
        return min(l, r)

# 정렬된 점 위에, 각 선분의 끝 점이 어디에 위치하는지 확인
# 1. 이분 탐색 중, 원하는 값이 있으면 해당 인덱스 반환
# 2. 이분 탐색 중, 원하는 값이 없으면
    # 2-1. 시작 점의 경우, 더 큰 index 선택
    # 2-2. 끝 점의 경우, 더 작은 index 선택
    
for _ in range(m):
    s, e = map(int, input().split())
    print(binary_search(e, False) - binary_search(s, True) + 1)