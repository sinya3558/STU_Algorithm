def is_prime_number(num):
    if num <= 1: return False
    if num == 2 or num == 3: return True
    for i in range(2, num // 2 + 1):
        if num % i == 0: return False
    return True


def solution(numbers):

    """
        00:09:45.89

        주어진 종이 조각을 붙여 만들 수 있는 소수의 개수 구하기
        1. 주어진 종이조각으로 만들 수 있는 수 찾기 → 순열
            1-1. 만약 이미 확인했던 수라면 건너뛰기
        2. 해당 수가 소수인지 확인
    """
    from itertools import permutations

    # 주어진 숫자 조각으로 순열 만들기
    cnt_prime_number = 0
    find_numbers = []
    for i in range(1, len(numbers) + 1):
        for num in permutations(numbers, i):

            # 튜플 형태의 데이터를 숫자로 변경
            num = int(''.join(num)) 

            # 이미 확인했던 수라면 건너뛰기
            if num in find_numbers:
                continue

            # 소수인지 판단
            find_numbers.append(num)
            if is_prime_number(num):
                cnt_prime_number += 1


    return cnt_prime_number


def main():
    print(solution("17"))
    print(solution("011"))


if __name__ == "__main__":
    main()