# https://www.acmicpc.net/problem/2075
""" 문제 : NxN matrix 에서 N 번째 큰 수를 출력해라. 
condition : nums are unique and randomly selected, but each nums in higher rows are greater to nums in the same col
binary tree? descending sort?
"""

import sys

# Get user inputs
user_inputs = int(sys.stdin.readline())
matrix = [] # empty matrix

# fill matrix (line by line)
for _ in range(user_inputs):
    row = list(map(int, sys.stdin.readline().split()))
    matrix.append(row)
# print(matrix)