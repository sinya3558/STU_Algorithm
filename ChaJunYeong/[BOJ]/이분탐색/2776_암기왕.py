import sys
def input():
    return sys.stdin.readline().rstrip()

# 이분 탐색으로 Search
# 탐색 대상인 배열은 정렬되어 있어야 함
# Middle 아이템 탐색
# 1. 찾고자 하는 아이템과 middle 아이템이 동일 → 참
# 2. 찾고자 하는 아이템이 middle보다 작으면, → 아이템이 배열의 왼쪽에 있음, r = middle - 1
# 3. 찾고자 하는 아이템이 middle보다 크면, → 아이템이 배열의 오른쪽에 있음, l = middle + 1
# 4. r < l 이 되는 순간, 아이템이 존재하지 않음

def search(num):
    l, r = 0, len(arr) - 1

    while l <= r:  
        mid = (l + r) // 2
        if arr[mid] == num:
            return 1
        if num < arr[mid]:
            r = mid - 1
        elif arr[mid] < num:
            l = mid + 1
    return 0


T = int(input())
for t in range(T):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    m = int(input())
    findnum = list(map(int, input().split()))

    for num in findnum:
        print(search(num))

