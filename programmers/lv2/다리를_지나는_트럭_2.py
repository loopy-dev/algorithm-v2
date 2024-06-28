'''
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

bridge_length는 1 이상 10,000 이하입니다.
weight는 1 이상 10,000 이하입니다.
truck_weights의 길이는 1 이상 10,000 이하입니다.
모든 트럭의 무게는 1 이상 weight 이하입니다.

'''
from collections import deque


def solution(bridge_length, weight, truck_weights):
    q = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    count = 0
    s = 0

    while q:
        s -= bridge.popleft()
        first = q[0]
        
        # 1. 총 무게의 합이 weight 이하인 경우
        if (s + first <= weight):
            bridge.append(q.popleft())
            s += first
        else:
            bridge.append(0)
        count += 1

    count += bridge_length

    return count


bridge_length = 10000
weight = 10
truck_weights = [10] * 10000
print(solution(bridge_length, weight, truck_weights))