import heapq


def solution(cap, n, deliveries, pickups):
    total = 0
    q1 = []
    q2 = []
    for i in range(n):
        if deliveries[i] or pickups[i]:
            heapq.heappush(q1, (-i, deliveries[i]))
            heapq.heappush(q2, (-i, pickups[i]))

    while q1 or q2:
        distance = 0
        current_amount = 0

        while q1:
            pos, amount = heapq.heappop(q1)
            distance = max(distance, -pos)
            if amount + current_amount <= cap:
                current_amount += amount
            else:
                heapq.heappush(q1, (pos, current_amount + amount - cap))
                break

        current_amount = 0
        while q2:
            pos, amount = heapq.heappop(q2)
            distance = max(distance, -pos)
            if amount + current_amount <= cap:
                current_amount += amount
            else:
                heapq.heappush(q2, (pos, current_amount + amount - cap))
                break

        total += (distance + 1) * 2

    return total


cap = 2
n = 7
deliveries = [0, 0, 0, 0, 0, 0, 0]
pickups = [0, 0, 0, 0, 0, 0, 0]
print(solution(cap, n, deliveries, pickups))
