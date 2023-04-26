def solution(storey):
    if storey <= 1:
        return storey

    answer = 0
    a = (storey // 10) * 10
    b = (storey // 10) * 10 + 10
    answer += min(storey - a + solution(a // 10), b - storey + solution(b // 10))
    return answer


# def solution(storey):
#     answer = solve(storey)
#     return answer


storey = 16
print(solution(storey))
