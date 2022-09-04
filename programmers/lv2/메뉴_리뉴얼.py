def solution(orders, course):
    answer = []
    arr = list(
        map(
            lambda x: "".join(x),
            list(map(lambda x: sorted(x), list(map(lambda x: list(x), orders)))),
        )
    )
    obj = {}
    for c in arr:
        dfs(0, "", obj, c)

    matrix = [[] for _ in range(11)]
    for key in obj.keys():
        if len(key) in course and obj[key] >= 2:
            matrix[len(key)].append((key, obj[key]))

    # sort
    for i in range(len(matrix)):
        matrix[i].sort(key=lambda x: -x[1])

    # append
    for i in range(len(matrix)):
        count = 0
        for el in matrix[i]:
            if el[1] >= count:
                answer.append(el[0])
                count = el[1]

    answer.sort()
    return answer


def dfs(idx, key, obj, order):
    if idx >= len(order):
        if key:
            obj[key] = obj.get(key, 0) + 1
        return

    dfs(idx + 1, key + order[idx], obj, order)
    dfs(idx + 1, key, obj, order)


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))
