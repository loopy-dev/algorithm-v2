from itertools import permutations


def calculate(a, b, operator):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    return False


def has_operator_included(check_list):
    for boolean in check_list:
        if boolean:
            return True
    return False


def get_priority_check_list(expression, priority):
    check_list = [False, False, False]
    for c in expression:
        if c == priority[0]:
            check_list[0] = True
        elif c == priority[1]:
            check_list[1] = True
        elif c == priority[2]:
            check_list[2] = True
    return check_list


def get_oprator(check_list, priority):
    if check_list[0]:
        return priority[0]

    if check_list[1]:
        return priority[1]

    return priority[2]


def solve(expression, priority):
    check_list = get_priority_check_list(expression, priority)

    # 숫자 반환
    if not has_operator_included(check_list):
        return int(expression)

    operator = get_oprator(check_list, priority)

    pieces = list(map(lambda x: solve(x, priority), expression.split(operator)))
    value = calculate(pieces[0], pieces[1], operator)

    for i in range(2, len(pieces)):
        value = calculate(value, pieces[i], operator)

    return value


def solution(expression):
    priorites = list(permutations(["-", "*", "+"]))
    answer = 0

    for priority in priorites:
        value = solve(expression, priority)
        answer = max(answer, abs(value))
    return answer


expression = "50*6-3*2"
print(solution(expression))
