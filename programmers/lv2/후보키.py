def is_key_minimal(arr, key):
    for k in arr:
        if (k & key) == k:
            return False
    return True


def is_unique_array(arr):
    return len(arr) == len(list(set(arr)))


def solution(relation):
    keys = []
    for i in range(1, 1 << len(relation[0])):
        arr = []

        # TODO: Check if i satisfies minimality
        if not is_key_minimal(keys, i):
            continue

        for j in range(len(relation)):
            temp = ""

            for k in range(len(relation[0])):
                if not (i & 1 << k):
                    continue

                temp += relation[j][k]

            arr.append(temp)

        if is_unique_array(arr):
            keys.append(i)

    return len(keys)


relation = [
    ["100", "ryan", "music", "2"],
    ["200", "apeach", "math", "2"],
    ["300", "tube", "computer", "3"],
    ["400", "con", "computer", "4"],
    ["500", "muzi", "music", "3"],
    ["600", "apeach", "music", "2"],
]

print(solution(relation))
