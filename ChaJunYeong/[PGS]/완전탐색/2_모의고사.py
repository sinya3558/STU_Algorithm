def solution(answers):
    answer = []

    """
        00:12:53.97
    """

    # 학생들이 찍는 방식
    students = {
        0: [1, 2, 3, 4, 5],
        1: [2, 1, 2, 3, 2, 4, 2, 5],
        2: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }

    cnt_correct_answer = [0, 0, 0]

    for i in range(len(answers)):
        for student in students:

            # 문제지의 정답과 학생의 답이 옳을 경우 + 1
            student_answers = students[student]
            repeat = len(students[student])
            if answers[i] == student_answers[i % repeat]:
                cnt_correct_answer[student] += 1

    # 가장 많은 정답을 맞춘 학생 찾기
    max_answer = max(cnt_correct_answer)
    for i in range(3):
        if max_answer == cnt_correct_answer[i]:
            answer.append(i + 1)
    return answer


def main():
    print(solution([1,2,3,4,5]))
    print(solution([1,3,2,4,2]))


if __name__ == "__main__":
    main()