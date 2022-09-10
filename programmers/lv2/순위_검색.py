from bisect import bisect_left

obj = {}


def get_count(query, score):
    arr = obj.get(query, [])
    return len(arr) - bisect_left(arr, score)


def backtrack(idx, query, info):
    if idx == len(info) - 1:
        obj[query] = obj.get(query, []) + [int(info[-1])]
        return

    backtrack(idx + 1, query + info[idx], info)
    backtrack(idx + 1, query + "-", info)


def create_query(info):
    for i in range(1 << 4):
        query = ""
        for j in range(4):
            if i & (1 << j):
                query += info[j]
            else:
                query += "-"
        obj[query] = obj.get(query, [])
        obj[query].append(int(info[-1]))


def solution(infos, queries):
    answer = []

    for info in infos:
        # backtrack(0, "", info.split(" "))
        create_query(info.split(" "))

    # sort
    for q in obj.keys():
        obj[q].sort()

    # query split and get score
    for query in queries:
        q = query.split(" ")
        answer.append(get_count("".join([q[0], q[2], q[4], q[6]]), int(q[-1])))

    return answer


info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50",
]
query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150",
]

print(solution(info, query))
