def solution(bridge_length, weight, truck_weights):
    answer = 1
    stack = [0 for i in range(bridge_length - 1)]
    stack.append(truck_weights.pop(0))

    trucks_weight_on_bridge = sum(stack)

    while trucks_weight_on_bridge > 0:
        answer += 1
        s = stack.pop(0)
        trucks_weight_on_bridge -= s

        if len(truck_weights) > 0:
            if trucks_weight_on_bridge + truck_weights[0] > weight:
                stack.append(0)
            else:
                truck = truck_weights.pop(0)
                trucks_weight_on_bridge += truck
                stack.append(truck)

    return answer


# bridge_length = 2
# weight = 10
# truck_weights = [7, 4, 5, 6]

# bridge_length = 100
# weight = 100
# truck_weights = [10]

bridge_length = 100
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

answer = solution(bridge_length, weight, truck_weights)
print(answer)
