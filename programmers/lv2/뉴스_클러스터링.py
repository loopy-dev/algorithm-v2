def intersection_count(a, b):

    count = 0
    s = set(list(a.keys()) + list(b.keys()))

    for key in s:
        count += min(a.get(key, 0), b.get(key, 0))
    return count


def union_count(a, b):
    count = 0
    s = set(list(a.keys()) + list(b.keys()))

    for key in s:
        count += max(a.get(key, 0), b.get(key, 0))
    return count


def is_empty(a):
    return not list(a.keys())


def slice_string(string):
    ret = []
    for i in range(len(string) - 1):
        flag = True
        sliced = string[i : i + 2]

        for c in sliced:
            if ord(c) < 97 or ord(c) > 122:
                flag = False
                break

        if flag:
            ret.append(sliced)
    return ret


def create_multiple_set(arr):
    ret = {}
    for key in arr:
        ret[key] = ret.get(key, 0) + 1
    return ret


def solution(str1, str2):
    # lower
    str1 = str1.lower()
    str2 = str2.lower()

    # 다중집합 만들기
    a, b = create_multiple_set(slice_string(str1)), create_multiple_set(
        (slice_string(str2))
    )

    similarity = 1
    if is_empty(a) and is_empty(b):
        return similarity * 65536

    similarity = intersection_count(a, b) / union_count(a, b)
    return int(similarity * 65536)


str1 = "E=M*C^2"
str2 = "e=m*c^2"
print(solution(str1, str2))
