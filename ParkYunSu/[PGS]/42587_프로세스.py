def solution(priorities, location):
    a = []#대기 중인 큐
    # 대기 중인 큐에 priorities값과 index 번호를 달아 줌
    for i in range(len(priorities)):
        a.append((priorities[i], i))
    count = 0
    while a:
        max_item = max(a, key = lambda x: x[0])
        b = a.pop(0)
        
        if b[0] < max_item[0]:
            a.append(b)
        else:
            count += 1
            if b[1] == location:
                return count