def solution(numbers, target):
    return solve(0, 0, numbers, target)


def solve(idx, number, numbers, target):
    if idx >= len(numbers):

        if number == target:
            return 1

        return 0

    answer = 0

    answer += solve(idx + 1, number + numbers[idx], numbers, target)
    answer += solve(idx + 1, number - numbers[idx], numbers, target)
    return answer


numbers = [4, 1, 2, 1]
target = 4

print(solution(numbers, target))
