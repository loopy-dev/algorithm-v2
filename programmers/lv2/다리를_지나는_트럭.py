from collections import deque


def solution(bridge_length, weight, truck_weights):
    q = deque([0] * bridge_length)
    left = deque(truck_weights)
    time = 0
    s = 0

    while q:
        s -= q.popleft()

        if left:
            next = left[0]
            if s + next <= weight:
                q.append(next)
                s += next
                left.popleft()
            else:
                q.append(0)

        time += 1

    return time


bridge_length = 100
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
print(solution(bridge_length, weight, truck_weights))
