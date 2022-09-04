from collections import deque


def cache_array(priorities):
    ret = [0 for _ in range(10)]

    for p in priorities:
        ret[p] += 1

    return ret


def is_most_important_document(p, cache):
    for i in range(p + 1, len(cache)):
        if cache[i] > 0:
            return False

    return True


def solution(priorities, location):
    cache = cache_array(priorities)
    q = deque()
    order = 0

    # initailize
    for i in range(len(priorities)):
        q.append((i, priorities[i]))

    while q:
        index, priority = q[0]

        # 가장 중요한 문서인지 확인
        if is_most_important_document(priority, cache):
            q.popleft()
            order += 1
            cache[priority] -= 1

            if index == location:
                return order

        else:
            q.rotate(-1)


priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))
