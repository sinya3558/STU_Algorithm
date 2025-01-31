import sys
def input():
    return sys.stdin.readline().rstrip()

postfix_input = list(map(str, input().split()))

operator = ['+', '-', '*', '/']
stack = list()

for char in postfix_input:
    if char not in operator:
        stack.append(char)

    else:
        b = int(stack.pop())
        a = int(stack.pop())
        
        if   char == '+': stack.append(a + b)
        elif char == '-': stack.append(a - b)
        elif char == '*': stack.append(a * b)
        elif char == '/': stack.append(a // b)

print(stack.pop())