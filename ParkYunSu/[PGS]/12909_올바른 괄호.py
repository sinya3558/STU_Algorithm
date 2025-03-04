def solution(s):
    answer=0
    for x in s:
        answer += 1 if x =='(' else -1
        
        if answer < 0:
            return False
    return answer==0