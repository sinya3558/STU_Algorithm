# 2nd trial
N = list(map(int, input()))
result = []

try:
    if (1<=N[0]<=20):
        for i in range(int(N[0])):
            N.append(input().split())

    for i in range(1, len(N), 1):
        if N[i][0].isdigit() and (0<int(N[i][0])<1000):
            N[i][0], N[i][1] = N[i][1], int(N[i][0])/2
        else:
            if N[i][0].replace(' ', '').lower().isalpha() and (0<len(N[i][0])<20):
                N[i][0], N[i][1] = N[i][0], int(N[i][1])
        result.append(N[i])
        result = sorted(result, key=lambda x: x[1])

    for i in range(len(result)):
        print(result[i][0])
        
except Exception as e:
    print('e:: ', e)
    

  
    
    
## 1st trial
# N = list(map(int, input()))
# if (1<=N[0]<=20):
#     for i in range(int(N[0])):
#         N.append(input().split())
#
# pair = [N[i+1] for i in range(0, len(N)-1)]
# result = []
#
# try:
#     for i in range(len(pair)):
#         if pair[i][0].isdigit():
#             result.append([pair[i][1], (int(pair[i][0])/2)])
#         else:
#             result.append([pair[i][0], int(pair[i][1])])
#
#     result = sorted(result, key=lambda x: x[1])
#
#     for i in range(len(result)):
#         print(result[i][0])
# except Exception as e:
#     print('e:: ', e)
    
    

'''
    time: 97 min(+43)
    status: fail(
        1st: runtime error.
        2nd: fail,
        3rd: fail
        )
    ref: 
    right answer:
    note:
         1. 세 번 모두 로컬에서는 잘 되는데 사이트에선 다 틀림. 깨끗한 머리로 하려고 다 다른날에 했는데도 다 틀림.
         2. 정답도 없음. java로 푼 블로그 글 하나 있음. 근데 정답률은 81%가 넘음.
         3. sys.stdin.realine, try-except, range limit, time limit -> 다 문제 없었음.
            C와 R로 쪼개는게 문제였던 것 같은데 아무리 해도 굳이 쪼개서 단계를 추가할 필요가 없어서 안했더니 또 실패.
         4. java 블로그 글에선 해쉬맵으로 바로 정리했는데, 나도 그러고 싶었다. 몽고디비 쓰면서 제이슨 형태는 이골이 나게 썼었고 나도 그 형태가 제일 편히디.
            근데 python에선 딕셔너리로 쓰는 것보다 이중 리스트로 쓰는게 지금까지 경험으로는 훨씬 간단했다. 그냥 인덱스로 불러오는게 낫지
            굳이 딕셔너리의 키값을 불러올 필요가 있나 싶고, 파이썬 해시맵 형태는 라이브러리 불러와야해서 코테에는 맞지 않다고 생각했다.
         5. 좋게 생각하면 로컬에선 잘 되고, 사이트에선 안되는 상황을 접한 경험, 해당 상황에 대한 에러 디버깅 시도에 가점.
         6. 해시맵 나도 정말로 너무나도 쓰고싶다. 근데 자바랑 비슷하지 않을 것 같아서 벌써부터 꼬일게 예상된다.
'''