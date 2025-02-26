def solution(brown, yellow):

    """
        00:14:31.14

        1. 노란색 격자무늬로 만들 수 있는 직사각형 크기 구하기기
            1-1. 약수 구하기와 동일
        2. 노란색 격자무늬로 만들어진 직사각형을 갈색 격자무늬로 덮었을 때 크기 구하기
            2-1. 이때, 주어진 갈색 격자무늬의 개수와 동일할 경우, 해당 경우가 정답이 됨
    """


    # 노란 격자무늬로 만들 수 있는 직사각형 크기 구하기
    yellow_rect = []

    # 만약 크기가 1이라면, (1, 1)로 초기화
    if yellow == 1:
        yellow_rect.append((1, 1))
    
    # 직사각형의 최솟값은 정사각형의 넓이와 동일하므로, height의 최댓값은 직사각형 넓이를 제곱근한 값과 동일함
    for yellow_h in range(1, int(yellow ** (1/2)) + 1):
        yellow_w = yellow // yellow_h
        if yellow % yellow_h == 0 and yellow_h <= yellow_w:

            # 계산한 갈색 격자무늬 갯수와 조건의 갈색 격자무늬 갯수가 동일할 경우 정답
            if brown == (yellow_w + 2) * 2 + yellow_h * 2:
                return [yellow_w + 2, yellow_h + 2]


def main():
    print(solution(10, 2))
    print(solution(8, 1))
    print(solution(24, 24))

if __name__ == "__main__":
    main()