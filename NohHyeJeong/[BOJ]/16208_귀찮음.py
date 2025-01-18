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
    
    파이썬 짜증난다
    생략을 무슨 이백개 해놨어 짜증나게
    
    sort가 관건인데 짜증난다
    정답코드 보면 생략 이백개 한거 생각하면 예상은 된다.
    이름이 귀찮음인데 생략 고리 채워야해서 더 귀찮아졌다 짜증난다
    
    담주에 이거랑 비슷한 문제 반드시 다시 푼다
'''