"""
Jesse and Cookies
Jesse는 모든 쿠키의 당도를 k이상으로 만들고 싶어한다.
sweetness = (1 * least sweet cookie + 2 * second least sweet cookie)
최소 횟수를 출력해야 한다.
가능하지 않다면 -1을 반환한다.
"""
"""
무식하게 해결해보기
1. 가장 작은 값과 그 다음으로 작은 값을 찾기
2. 합친 다음 다시 다음 다시 그 값을 배열에 넣기

heapq 자료 구조를 이용한다면 시간상으로 조금 더 이득을 볼 수 있을 듯
"""
import heapq


def raise_sweetness(a, b):
    """
    a: least sweet cookie
    b: second least sweet cookie
    """
    return a + 2 * b


def cookies(k, q):
    count = 0
    heapq.heapify(q)

    while q:
        if len(q) < 2 and q[0] < k:
            return -1

        if len(q) < 2:
            break

        least = heapq.heappop(q)
        second_least = heapq.heappop(q)

        if least >= k:
            return count

        new_sweetness = raise_sweetness(least, second_least)
        heapq.heappush(q, new_sweetness)
        count += 1

    return count
