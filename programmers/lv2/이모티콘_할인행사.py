def backtrack(array, current, length):
    if len(current) == length:
        array.append(current[:])
        return

    for discount in [10, 20, 30, 40]:
        current.append(discount)
        backtrack(array, current, length)
        current.pop()


def solution(users, emoticons):
    total_count = 0
    total_value = 0
    perms = []

    # list 우선 구하기
    backtrack(perms, [], len(emoticons))

    for p in perms:
        count = 0
        value = 0

        for user in users:
            discount, standard_value = user
            emoticon_value = 0
            flag = False

            for i in range(len(p)):
                if p[i] >= discount:
                    emoticon_value += emoticons[i] * (100 - p[i]) // 100

            if emoticon_value >= standard_value:
                flag = True

            if flag:
                count += 1
                continue

            value += emoticon_value

        if count > total_count:
            total_count = count
            total_value = value
        elif count == total_count:
            total_value = max(total_value, value)

    return [total_count, total_value]


users = [
    [40, 2900],
    [23, 10000],
    [11, 5200],
    [5, 5900],
    [40, 3100],
    [27, 9200],
    [32, 6900],
]
emoticons = [1300, 1500, 1600, 4900]
print(solution(users, emoticons))
