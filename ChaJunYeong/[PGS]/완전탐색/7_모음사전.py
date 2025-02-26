"""
    00:37:54.06
"""

def solution(word):
    answer = 0

    word_flag = False
    string = "AEIOU"
    def make_word(depth, s):
        nonlocal answer, word_flag

        # 단어를 찾았을 때 word_flag를 True로 만들면서 break
        if s == word:
            word_flag = True
            return
        
        # 단어의 최대 길이에 도달하면 되돌아가기
        if depth == 5:
            return
        
        # AEIOU 하나씩 대입
        for i in range(5):
            answer += 1
            make_word(depth + 1, s + string[i])
            if word_flag:
                return

    make_word(0, '')
    return answer


def main():
    print(solution("AAAAE"))
    print(solution("AAAE"))
    print(solution("I"))
    print(solution("EIO"))


if __name__ == "__main__":
    main()