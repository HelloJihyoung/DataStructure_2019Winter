def solution(bridge_length, weight, truck_weights):
    # queue 다리 길이만큼
    bridge = [0] * bridge_length
    time = 0
    while bridge:
        time += 1
        bridge.pop(0)
        if truck_weights:
            if truck_weights[0] + sum(bridge) <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return time


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))