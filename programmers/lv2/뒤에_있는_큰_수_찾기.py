def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
        number = numbers[i]
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number

        stack.append(i)

    return answer


numbers = [9, 1, 5, 3, 6, 2]
print(solution(numbers))
