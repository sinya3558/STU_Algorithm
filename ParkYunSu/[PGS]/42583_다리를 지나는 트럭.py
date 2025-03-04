from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    total_weight = 0
    while trucks or total_weight > 0:
        answer += 1
        total_weight -= bridge.popleft()
        if trucks:
            if total_weight + trucks[0] <= weight:
                new_truck = trucks.popleft()
                bridge.append(new_truck)
                total_weight += new_truck
            else:
                bridge.append(0)
    return answer