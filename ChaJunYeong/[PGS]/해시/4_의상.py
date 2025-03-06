def solution(clothes):

    """
        00:16:01.22
        
        서로 다른 옷 조합의 수 구하기

        조건 1 : 각 종류별로 최대 1가지 의상만 착용 가능
        조건 2 : 착용한 의상의 일부가 겹치더라도 다른 의상이 겹치지 않은 조합이면 가능
        조건 3 : 의상을 추가로 더 착용한 경우에도 가능
        조건 4 : 최소 한 개의 의상을 입음

        풀이:
            의상의 이름이 중요하지 않음. 중요한 것은 같은 종류의 옷이 몇 벌이 있는가.
            1. 같은 종류의 옷끼리 갯수 세기
            2. 각 종류의 옷을 입어보는 경우의 수는 각 종류의 옷 + 1 (해당 종류의 옷을 선택하지 않은 경우)
            3. 전체 경우의 수는 2에서 구한 값에 전체 옷을 입어보지 않은 경우 제외 -1
    """

    from collections import Counter

    categories = Counter([category for _, category in clothes])
    answer = 1
    for value in categories.values():
        answer *= (value + 1)
    return answer - 1


def main():
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
    print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))


if __name__ == "__main__":
    main()
