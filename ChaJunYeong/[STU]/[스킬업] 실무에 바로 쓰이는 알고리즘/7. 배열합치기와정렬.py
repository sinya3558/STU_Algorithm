import sys
def input():
    return sys.stdin.readline().rstrip()

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

def merge(arr1, arr2):
    res = []
    idx1, idx2 = 0, 0

    while idx1 < len(arr1) and idx2 < len(arr2):
        if arr1[idx1] <= arr2[idx2]:
            res.append(arr1[idx1])
            idx1 += 1
        else:
            res.append(arr2[idx2])
            idx2 += 1

    if   idx1 == len(arr1): res += arr2[idx2:]
    elif idx2 == len(arr2): res += arr1[idx1:]
    return res

def mergesort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

print(mergesort(arr1 + arr2))