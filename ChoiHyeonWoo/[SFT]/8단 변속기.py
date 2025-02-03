gear = list(map(int, input().split()))
check_1 = [1, 2, 3, 4, 5, 6, 7, 8]
check_2 = [8, 7, 6, 5, 4 ,3, 2, 1]
if gear == check_1:
    print('ascending')
elif gear == check_2:
    print('descending')
else:
    print('mixed')