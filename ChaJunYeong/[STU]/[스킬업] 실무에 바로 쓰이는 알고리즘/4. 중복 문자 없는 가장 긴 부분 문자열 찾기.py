import sys
def input():
    return sys.stdin.readline().rstrip()

s = input()

char_index = {} # 문자의 마지막 위치 저장
result = 0      # 최대 부분 문자열 길이이
start = 0       # 현재 부분 문자열의 시작점

for i, char in enumerate(s):
    # 중복되는 순간 시작점 위치치 옮김
    if char in char_index and char_index[char] >= start:    
        start = char_index[char] + 1

    char_index[char] = i    # 현재 위치로 갱신
    result = max(result, i - start + 1)

print(result)