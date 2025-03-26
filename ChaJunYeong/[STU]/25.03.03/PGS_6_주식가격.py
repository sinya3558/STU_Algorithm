'''
prices = 초 단위의 가격

[1, 2, 3, 2, 3]
[4, 3, 1, 1, 0]
입력된 배열의 길이 = 총 주가 기록 시간 (5초)
'''

from collections import deque
def solution(prices):
    answer = []              # 각 시점별로 계산한 '떨어지지 않은 시간'을 저장할 리스트
    dq = deque(prices)       # 리스트를 덱(deque)으로 변환 (popleft() 시 O(1)로 처리)

    while dq:                # 덱에 데이터가 남아 있는 동안 반복
        current = dq.popleft()  
        # 덱의 맨 왼쪽(가장 오래된) 데이터를 꺼냄. 
        # 이 current 값에 대해 '다음 주가들과 비교하여 떨어지지 않은 기간'을 측정할 예정
        
        count = 0            # 현재 시점에서 '가격이 떨어지지 않은 기간(초)'을 셀 변수
        
        for price in dq:     # 남아 있는 주가들을 순차적으로 확인
            if current <= price:
                # 만약 '현재 주가'가 이후 시점의 주가보다 작거나 같다면
                # 가격이 떨어지지 않은 것으로 판단하여 count를 1 증가
                count += 1
            else:
                # 만약 '현재 주가'가 이후 시점의 주가보다 크면
                # 여기서 count를 1 증가시키고(해당 순간 '떨어졌음'을 기록)
                # 루프를 즉시 종료한다.
                count += 1
                break
                
            # 해당 코드 구조상, 반복문을 돌 때마다 answer에 count 값을 계속 추가하게 됨.
            answer.append(count)
            
    return answer
