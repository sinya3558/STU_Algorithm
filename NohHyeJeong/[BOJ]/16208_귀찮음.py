n = input() #number
l = input().split(' ') #length
c = 0 #cost


# str to int
def to_int(li: list):
    tmp = []
    for i in range(len(li)):
        tmp.append(int(li[i]))
    return tmp


# odd case, check and send
def check_which(li1: list, li2: list, li3: list, li4: list):
    if sum(li1)*sum(li2) == sum(li3)*sum(li4):
        pass
    else:
        if sum(li1)*sum(li2) > sum(li3)*sum(li4):
            return li3, li4
        else: #<
            return li1, li2
            
            
# calculate  
def calculate(li1: list, li2: list):
    return sum(li1)*sum(li2)


# select and divide
def divide(li: list):
    tmp1 = li[:int(len(li)/2)] 
    tmp2 = li[int(len(li)/2):]
    
    tmp3 = li[:int(len(li)/2)+1] #-1 if odd
    tmp4 = li[int(len(li)/2)+1:] #-1 if odd

    if len(li)%2: #odd
        tmp1, tmp2 = check_which(tmp1, tmp2, tmp3, tmp4)
        return tmp1, tmp2
    else: #even
        return tmp1, tmp2



if int(n) == int(len(l)): # length check if equal   
    tmp=to_int(l)
    tmp2 = tmp
    
    for i in range(int(len(l)/2)):
        ###
        pass




'''
    time: over 2hrs
    status: fail(overtime)
    ref: https://ckstjr.tistory.com/91
    right answer:
        n = int(input())
        A = list(map(int, input().split()))
        A.sort()

        stick_len = sum(A)
        result = 0
        
        for a in A:
            stick_len -= a
            result += a * stick_len

        print(result)
    solution:
        1. map(): iterator, 단독으로는 시각화 불가능하고 list() 붙여야 가능.
           !!! 파이썬 dictionary, 자바 hashmap, 자바스크립트 object와는 다름. !!!
        2. Greedy algorithm, 언제나 최소 사이즈를 먼저 잘라야 비용 최소화
           나의 경우 트리처럼 중간부터 들어가서 꼬임.
'''