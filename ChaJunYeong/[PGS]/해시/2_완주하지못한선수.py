def solution(participant, completion):
    """
        00:05:28.41

        단 한 명의 선수를 제외하고 모든 선수가 마라톤 완주
        마라톤에 완주하지 못한 선수

        조건 1 : 참가자 중에는 동명이인이 있을 수 있음

        풀이 :
            1. 참가자와 완주자를 정렬
            2. 리스트 앞에서부터 하나씩 돌면서 완주자와 참가자 이름이 동일한지 확인
                2-1. 동일하지 않으면 참가자가 완주하지 못함
                2-2. 만약 완주자 리스트를 끝까지 돌았을 때 완주하지 못한 사람이 없으면, 참가자중 마지막 사람이 미완주자
    """

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


def hash_solution(participant, completion):

    """
        https://codingdog.tistory.com/entry/python-hash-%ED%95%A8%EC%88%98%EC%97%90-%EB%8C%80%ED%95%B4-%EC%95%8C%EC%95%84%EB%B4%85%EC%8B%9C%EB%8B%A4

        해시 : 데이터를 효율적으로 관리하기 위해 임의의 길이의 데이터를 고정된 길이의 데이터로 매핑
            key : 매핑하기 전 원래 데이터의 값
            value : 매핑 후 데이터의 값

        파이썬에는 hash 함수를 통해 데이터에 값에 따른 hash 값을 확인할 수 있음
        (일반적으로 데이터 값이 동일하면, 해시 값도 동일)

        https://fierycoding.tistory.com/68
        https://velog.io/@eunhye_/python-collections-Counter

        해시를 활용한 자료구조 : dictionary, Counter
        dictionary의 경우, key 값으로 들어가는 데이터는 hash 값으로 변경된 후, hash-talbe의 hash 값에 value 데이터가 들어가는 구조
        해시 테이블을 활용해 dictionary를 구성했을 때, get, insert, update, delete, search 기능의 시간복잡도가 O(1)에 수렴하는 장점
        counter 역시, hash를 활용하여 iterator의 데이터 개수를 세어주는 클래스        
    """

    # hash를 활용한 문제 풀이
    hash_loser=sum([hash(a) for a in participant])-sum([hash(a) for a in completion])
    for a in participant:
        if hash(a)==hash_loser:
            return a
        

def main():
    print(hash_solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
    print(hash_solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
    print(hash_solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))


if __name__ == "__main__":
    main()

