"""
귤 고르기
많은 순서대로 배치하고 가장 많은 순서대로 담는다.
"""


def solution(k, tangerine):
    cache = {}
    for i in range(len(tangerine)):
        size = tangerine[i]
        cache[size] = cache.get(size, 0) + 1

    arr = []
    for key, value in cache.items():
        arr.append((key, value))

    # 숫자가 많은 순서대로 정렬
    arr.sort(key=lambda x: -x[1])

    s = 0
    for i in range(len(arr)):
        s += arr[i][1]

        if s >= k:
            return i + 1

    return len(arr)


k = 2
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))
