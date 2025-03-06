def solution(nums):

    """
        00:09:18.80
    
        N 마리의 폰켓몰 중 N/2 마리를 가져가야 함.
        이때, 최대한 다양한 종류의 폰켓몬을 가지고 싶음.

        조건 1 : nums <= 10,000 는 항상 짝수로 주어짐
        조건 2 : 폰켓몬 종류 번호는 200,000 이하의 자연수수

        풀이 : 
            조합에 상관 없이, 폰켓몬 종 수에 따라 답이 결정됨
            1. 폰켓몬의 종류가 N/2 보다 많으면, N/2 만큼 다양한 종류의 폰켓몬 확보
            2. 폰켓몬의 종류가 N/2 보다 작으면, 폰켓몬의 종류만큼 다양한 종류의 폰켓몬 확보
    """
    
    maximum = len(nums) // 2
    species = len(set(nums))
    return maximum if maximum <= species else species
        

def main():
    print(solution([3, 1, 2, 3]))
    print(solution([3, 3, 3, 2, 2, 4]))
    print(solution([3, 3, 3, 2, 2, 2]))


if __name__ == "__main__":
    main()

