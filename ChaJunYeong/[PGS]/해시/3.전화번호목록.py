def solution(phone_book):

    """
        00:12:00.07

        어떤 전화 번호가 다른 전화 번호의 접두어인 경우가 있으면 False, 그렇지 않으면 True
        ex)
            구조대 : 119
            지영석 : 1195524421
            구조대는 지영석 전화번호의 접두어이다.

        조건 1 : phone book의 길이는 1,000,000
        조건 2 : 각 전화번호의 길이의 최댓값은 20
        조건 3 : 같은 전화번호가 중복해서 들어가 있지 않음

        풀이 : 
            번호가 작은 전화번호 부터 비교
                1. 전화번호를 string 상태에서 정렬한 후
                2. 정렬된 전화번호에서 앞 전화번호와 바로 뒷 전화번호 끼리 비교
    """

    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    return True


def hash_solution(phone_book):

    """
        https://school.programmers.co.kr/learn/courses/30/lessons/42577/solution_groups?language=python3
        해시를 활용한 문제 풀이
    """

    hash_map = {num : 1 for num in phone_book}
    for phone_number in phone_book:
        temp = ""
        for num in phone_number:
            temp += num

            # 만들어진 전화번호가 자기 자신을 제외하고 hash map에 존재할 경우 False
            # 1번 예시의 경우, 1195524421에서 119까지 만들었을 때 전화번호가 존재하므로 False
            if temp in hash_map and temp != phone_number:
                return False
    return True

def main():
    print(hash_solution(["119", "97674223", "1195524421"]))
    print(hash_solution(["123","456","789"]))
    print(hash_solution(["12","123","1235","567","88"]))


if __name__ == "__main__":
    main()
