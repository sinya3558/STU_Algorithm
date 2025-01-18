c = int(input())
for i in range(c):
    n,m = map(int,input().split())
    FIFO = list(map(int,input().split()))
    order_list = [x for x in range(len(FIFO))]
    
    cnt = 0
    while True:
        if FIFO[0] >= max(FIFO):
            cnt += 1
            if order_list[0] == m:
                break
            else:
                FIFO = FIFO[1:]
                order_list = order_list[1:]
        else:
            FIFO = FIFO[1:] + FIFO[:1]
            order_list = order_list[1:] + order_list[:1]
    print(cnt)