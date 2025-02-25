from collections import deque

def solution(bridge_length, weight, truck_weights):

    """
        모든 트럭이 다리를 건너는데 걸리는 최소 시간
        
        조건:
            1. 다리에는 트럭이 최대 bridge_length 만큼 올라갈 수 있음
            2. 다리는 weight 이하의 무게만큼 버틸 수 있음
            3. 트럭은 한 번에 한 개씩 순서대로 올라갈 수 있음

        00:57:47.700
        
        큐로 풀이 할 수 있을 것 같은데...
        풀이:
            가장 중요한 것은 마지막 트럭이 올라간 순간의 시간 + 다리 길이
            1. 트럭 대기 (다리 길이와 트럭 무게 조건으로 올라갈 수 있는지 확인)
                1-1. 올라갈 수 있다면, 트럭 무게와 올라간 순간의 시간 측정
                1-2. 올라갈 수 없다면, 가장 먼저 들어간 트럭 제거
            2. 트럭이 다 들어갔다면, 가장 마지막에 트럭이 올라간 시간 + 다리길이 정답 출력력
                
    """

    truck_on_bridge_weight = 0
    bridge = deque()
    time = 1
    
    for truck in truck_weights:
        while True:
            # 올라갈 수 있는지 조건 확인 (조건 만족되면, 트럭 무게와 올라간 시간 기록)
            if len(bridge) + 1 <= bridge_length and truck_on_bridge_weight + truck <= weight:
                truck_on_bridge_weight += truck
                bridge.append((truck, time))
                time += 1
                break

            # 올라갈 수 없다면, 먼저 올라간 트럭 제거
            # 이때, 저장해 둔 트럭 무게로 다리에 올라간 트럭 전체 무게에서 빼기
            # 또한, 해당 트럭이 다리를 건너는데 걸리는 시간 측정 (이때, 현재 시간과 현재 트럭이 다리를 건너는데 걸리는 시간 중 큰 값으로 결정)
            else:
                pre_weight, pre_time = bridge.popleft()
                truck_on_bridge_weight -= pre_weight
                time = max(time, pre_time + bridge_length)

    last_weight, last_time = bridge.pop()
    return last_time + bridge_length


print(solution(2, 10, [7, 4, 5, 6]))    # 8
print(solution(3, 15, [7, 6, 3, 2]))    # 8
print(solution(100, 100, [10])) # 101
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])) # 110
print(solution(10, 100, [50, 10, 10, 10, 10, 60, 30]))  # 24
print(solution(10, 100, [50, 30, 10, 10, 30, 10, 40]))  # 23
