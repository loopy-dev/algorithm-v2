def solution(n):
    iss1 = [False] * n
    iss2 = [False] * 2 * n
    iss3 = [False] * 2 * n
    return backtrack(0, iss1, iss2, iss3, n)


def backtrack(y, iss1, iss2, iss3, n):
    if y == n:
        return 1
    count = 0
    for x in range(n):
        if not iss1[x] and not iss2[y + x] and not iss3[n - 1 + y - x]:
            iss1[x], iss2[y + x], iss3[n - 1 + y - x] = True, True, True
            count += backtrack(y + 1, iss1, iss2, iss3, n)
            iss1[x], iss2[y + x], iss3[n - 1 + y - x] = False, False, False
    return count


n = 4
print(solution(n))
