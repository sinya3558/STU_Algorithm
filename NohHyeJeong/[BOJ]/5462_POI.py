import sys
input = sys.stdin.readline

N, T, P = input().split() # num of peoples, num of problems, position of
ls = [input().strip().split(' ') for _ in range(int(N)) if (1<=int(N)<=2000) and (1<=int(T)<=2000) and (1<=int(P)<=int(N))]
tp = [int(j) for i in range(len(ls)) for j in ls[i]]


# 각 문제별 점수
score_of_problems = [0 for _ in range(int(T))]
answer_of_persons = []

for i in range(0, len(tp), int(T)): # col1
    tmp1 = tp[i:i+int(T)]
    tmp2 = ''
    
    for j in range(len(tmp1)):
        tmp2 = tmp2 + str(tmp1[j])
        if tmp1[j] == 0:
            score_of_problems[j]  = score_of_problems[j]+1 # 개별 문제별 점수 ++
    answer_of_persons.append(tmp2) # 개별 제출 답안들


# # 각 사람별 점수
score_of_persons = [0 for _ in range(int(N))]
for i in range(len(answer_of_persons)):
    tmp = list(answer_of_persons[i])
        
    for j in range(len(tmp)):
        if int(tmp[j]) == 1: 
            score_of_persons[i] = score_of_persons[i] + score_of_problems[j]


# 문제 맞은 갯수 합
def count_one(input):
    ls = list(input)
    sums = sum(1 for i in range(len(ls)) if int(ls[i]) == 1)
    return(sums)


# for ranking
more = 0
tie_prob = 0
tie_id = 0

for i in range(len(score_of_persons)):
    if (i != int(P)-1):
        if (score_of_persons[i] > score_of_persons[int(P)-1]):
            more += 1
        elif (score_of_persons[i] == score_of_persons[int(P)-1]):
            if count_one(answer_of_persons[i]) > count_one(answer_of_persons[int(P)-1]):
                tie_prob +=1
            elif count_one(answer_of_persons[i]) == count_one(answer_of_persons[int(P)-1]):
                if (i < (int(P)-1)):
                    tie_id += 1



print(more + tie_prob + tie_id + 1)


'''
    time: over 2hrs
    status: fail
    ref: cgpt
    algorithm type: sorting + ranking
    right answer:
        import sys
        input = sys.stdin.readline

        # 입력 처리
        N, T, P = map(int, input().split())

        # 입력값 예외 처리
        if not (1 <= N <= 2000 and 1 <= T <= 2000 and 1 <= P <= N):
            print("입력값이 제한을 초과합니다.")
            exit()

        # 데이터 입력 및 예외 처리
        ls = []
        for _ in range(N):
            row = list(map(int, input().split()))
            
            # 문제 개수(T)와 입력된 데이터 개수가 다르면 오류
            if len(row) != T:
                print("잘못된 입력입니다.")
                sys.exit(1)
            
            ls.append(row)

        # 각 문제별 점수 계산
        score_of_problems = [0] * T
        for person in ls:
            for j in range(T):
                if person[j] == 0:
                    score_of_problems[j] += 1

        # 각 사람별 점수 계산
        score_of_persons = [0] * N
        for i in range(N):
            for j in range(T):
                if ls[i][j] == 1:
                    score_of_persons[i] += score_of_problems[j]

        # P번째 참가자의 정보
        P_idx = P - 1
        target_score = score_of_persons[P_idx]
        target_correct = sum(ls[P_idx])

        # 순위 계산
        more = 0
        tie_prob = 0
        tie_id = 0

        for i in range(N):
            if i == P_idx:
                continue
            if score_of_persons[i] > target_score:
                more += 1
            elif score_of_persons[i] == target_score:
                if sum(ls[i]) > target_correct:
                    tie_prob += 1
                elif sum(ls[i]) == target_correct and i < P_idx:
                    tie_id += 1

        # 최종 순위 출력
        print(more + tie_prob + tie_id + 1)
        
        결론: 코드 수정 사항
            입력값을 map(int, input().split())으로 변환하여 정수형으로 다룸.
            리스트 입력 부분을 map(int, input().split())으로 수정하여 효율적으로 입력 처리.
            문제별 점수(score_of_problems)를 0 개수로 정확하게 계산.
            사람별 점수(score_of_persons)를 1인 경우에만 점수를 합산하도록 수정.
            순위 비교에서 동점자 처리 로직을 정확하게 수정.
    note:
        1. 두 에러는 안떠서 다행인건가? 나름 튜플이랑 단순경로 사용하려고 노력했는데, 그리고 낼 때는 나름 만족했는데, 지피티 답안 보니까 또..ㅋㅋㅋㅋㅋㅋㅋ 하
        2. 지금 방식으로 두 개 정도 더 풀어보고 총 세개 부족한 점 합쳐서 다음에 적용하고 싶은데, 그러기엔 당장 다음 문제에서부터 그 부분들이 신경쓰일 거 안다.
        3. 부족한 점은 아래와 같다.
            1) 입력값이 범위를 넘어서면 exit()으로 내보내기
            2) 처음 입력 받을때부터 map(타입, @@@) 식으로 형변환해서 값 저장.
            3) 혼동 올 수 있으니, 변수 초기에 지정하고 시작.
            4) 괜히 for 돌리지 말고, [0] * n 으로 원하는 사이즈의 1차원 리스트 생성.
            5) continue/break/pass/yield 구분 확실히 해야한다. 생각보다 뭉뚱그려서 알고 있었다.
        4. 이거 적용해도 또 틀랄 것 같긴 한데, 그래도 조금씩 범위를 줄여나가자.
'''