def solution(sizes):

    """
        00:33:11.71

        1. 큰 것들 중 최댓값 구하기
        2. 작은 것들 중 최댓값 구하기
    """

    first_max_length  = -1
    second_max_length = -1

    for w, h in sizes:
        if w >= h:
            first_max_length  = max(first_max_length,  w)
            second_max_length = max(second_max_length, h)
        elif w < h:
            first_max_length  = max(first_max_length,  h)
            second_max_length = max(second_max_length, w)

    return first_max_length * second_max_length

    


def main():
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
    print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))


if __name__ == "__main__":
    main()