N, M = list(map(int, input().split(' '))) # num of det, num of hous
lst = [input().split(' ') for _ in range(N)] # input

obj = {int(p): int(c) for p, c in lst if (1<=int(p)<int(M)) and (1<=int(c)<=1000000000)} # placed, calls
obj = dict(sorted(obj.items()))

if int(N)+1 == int(M):
    print(max(obj.values()))
else:
    tmp = list(obj.values())
    res = obj[min(obj.keys())]
    
    for i in range(len(tmp)-1):
        if ((tmp[i] - tmp[i+1])>0):
            res = (tmp[i] - tmp[i+1])
        else:
            res += sum(tmp[i+1:])
    print(res) # result


'''
    time: 116 min
    status: fail(
        1st: Time Limit Error,
        2nd: Runtime Error
        )
    ref: cgpt
    algorithm type: greedy
    right answer:
        def main():
            import sys
            input = sys.stdin.read
            data = input().split()
            
            N = int(data[0])
            M = int(data[1])
            
            detectors = []
            index = 2
            for _ in range(N):
                P = int(data[index])
                C = int(data[index + 1])
                detectors.append((P, C))
                index += 2
            
            # 감지기 위치를 기준으로 정렬
            detectors.sort()
            
            # 최소 통화량 계산
            min_calls = 0
            current_min = float('inf')
            
            for _, C in detectors:
                if C < current_min:
                    current_min = C
                min_calls += current_min
            
            print(min_calls)
        if __name__ == "__main__":
            main()
    note:
         1. 다양한 에러를 보고 있다. 런타임 에러에 이어서 이번엔 시간초과다. 각 에러가 일어나는 이유좀 찾아봤다.
            - Runtime Error
            1) 문제에 나온 인풋 값들의 범위
            2) 0으로 나누기
            3) 없는 키 조회
            4) 재귀 깊이 초과
            5) 메모리 초과
            - Time Limit Error
            1) 시간복잡도 문제
            2) 인풋 하는 방식(sys.stdin.read 사용 권장)
            3) 불필요한 단계 수행
            4) 중복 재귀 호출
         2. 해결방안은 접근 방식을 다양화 하고(1), 최대한 단순하게 반복문을 짜거나(4) 딕셔너리로 바로 값 받아오는 방식(4)으로 코드 짤 것.
         3. 문제 예시가 조금 더 복장합 게 있었다면 하는 아쉬움이 있다. 정답은 나오지만 아직도 문제가 좀 이해가 안간다.
         4. 문제는 리스트였다. 리스트 앞으로 안쓴다. 특히 이중이 오브젝트랑 형태가 비슷해서 편해서 많이 썼는데 지금보니 최악이다.
         5. 이중 루프도 여기선 확실히 문제일 수 있다. 나는 삼중 루프까지도 자주 써왔다. 앞으로 안쓴다.
         6. 메모이제이션 적극 활용하자. 
'''