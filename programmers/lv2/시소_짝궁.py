from bisect import bisect_left, bisect_right


# sort
# ratio == 1 -> bisect_right() - bisect_left() > 1 => ok
# ratio == 4 / 3, 3 / 2, 4 / 2 -> 숫자가 존재하는지 확인
def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


def factorial(n):
    if n <= 0:
        return 1

    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer


def solution(weights):
    s = set()
    answer = 0

    for i in range(len(weights)):
        s.add(weights[i])

    weights.sort()

    numbers = sorted(list(s))

    for i in range(len(numbers)):
        number = numbers[i]
        length = bisect_right(weights, number) - bisect_left(weights, number)

        # ratio == 1
        answer += combination(length, 2)

        # ratio == 3 / 2
        if number % 3 == 0 and number * 2 // 3 in s:
            answer += length * (
                bisect_right(weights, number * 2 // 3)
                - bisect_left(weights, number * 2 // 3)
            )

        # ratio == 4 / 3
        if number % 4 == 0 and number * 3 // 4 in s:
            answer += length * (
                bisect_right(weights, number * 3 // 4)
                - bisect_left(weights, number * 3 // 4)
            )

        # ratio == 2
        if number * 2 in s:
            answer += length * (
                bisect_right(weights, number * 2) - bisect_left(weights, number * 2)
            )

    return answer


weights = [100, 100, 100, 150, 150, 200, 300]
print(solution(weights))
