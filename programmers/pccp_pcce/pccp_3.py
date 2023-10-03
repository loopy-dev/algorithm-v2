# 유전 법칙


def check(index, depth):
    if depth <= 0:
        return "Rr"

    parent = check(index // 4, depth - 1)

    if parent == "RR":
        return "RR"

    if parent == "rr":
        return "rr"

    idx = index % 4

    if idx == 0:
        return "RR"

    if idx == 3:
        return "rr"

    return "Rr"


def solution(queries):
    answer = []
    for query in queries:
        depth, index = query
        answer.append(check(index - 1, depth - 1))
    return answer


queries = [[3, 5]]
print(solution(queries))
