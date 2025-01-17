N = input()


def calculate(num):
    width1 = 0 # 작은 width
    width2 = 1 # 큰 width
    tmp = 0

    for i in range(int(num)):
        tmp = width1 + width2
        width1 = width2
        width2 = tmp
    return (2*width1 + 2*width2)


print(calculate(N))
