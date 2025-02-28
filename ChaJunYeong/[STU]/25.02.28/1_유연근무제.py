def solution(schedules, timelogs, startday):

    """
        각자 설정한 출근 희망 시각에 늦지않고 출근한 직원에게 상품 주기
        이때, 모든 시각은 시에 100을 곱하고 분을 더한 정수

        조건 1 : 직원은 자신이 설정한 출근 희망 시각 + 10분 까지 어플로 출근해야함
        조건 2 : 토요일, 일요일의 출근 시각은 이벤트에 영향 주지 않음
        조건 3 : 직원은 매일 한 번 씩 어플로 출근

        목표 : 직원이 설정한 출근 희망 시각과 실제로 출근한 기록을 바탕으로 상품을 받을 직원이 몇명인지 출력

        풀이 : 
            1. 토요일, 일요일이 몇번째 날인지 확인
                startday = 1이면 월요일
            2. 앞선 직원 부터 차례대로 맞게 출근했는지 확인
                2-1. 만약 이전에 제대로 출근하지 않았다면 확인 하지 않음
    """

    answer = 0
    for idx in range(len(schedules)):

        # 1. 직원의 희망 출근 시각 범위
        s = schedules[idx]
        e_hour = s // 100
        e_min  = s % 100 + 10
        if 60 <= e_min:
            e_hour += 1
            e_min = e_min % 60
        e = e_hour * 100 + e_min

        # 2. 주말은 제외한 나머지 날짜에 제대로 출근했는지 확인
        pass_flag = True
        for i in range(7):
            if (startday + i) % 7 == 6 or (startday + i) % 7 == 0: # 토요일 or 일요일
                continue

            if not (timelogs[idx][i] <= e):
                pass_flag = False
                break

        if pass_flag: 
            answer += 1
    
    return answer



def main():
    print(solution([700, 800, 1100], [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]], 5))
    print(solution([730, 855, 700, 720], [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]], 1))



if __name__ == "__main__":
    main()