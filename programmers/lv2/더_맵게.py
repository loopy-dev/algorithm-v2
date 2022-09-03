import heapq


def solution(scoville, k):
    heapq.heapify(scoville)
    count = 0

    while scoville:
        k1 = heapq.heappop(scoville)

        if k1 >= k:
            return count

        if not scoville:
            return -1

        k2 = heapq.heappop(scoville)
        k3 = k1 + k2 * 2
        heapq.heappush(scoville, k3)
        count += 1

    return -1


scoville = [1, 2]
k = 3
print(solution(scoville, k))
