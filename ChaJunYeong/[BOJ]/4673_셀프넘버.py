flag = [True for _ in range(10001)]

for num in range(1, 10001):
    total = num

    strnum = str(num)
    for each in strnum:
        total += int(each)

    if total <= 10000:
        flag[total] = False
    
for num in range(1, 10001):
    if flag[num]:
        print(num)