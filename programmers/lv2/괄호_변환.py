def get_minimum_balanced_braket_index(brakets):
    left = 0
    right = 0
    for c in brakets:
        if c == "(":
            left += 1
        else:
            right += 1
        if left == right:
            return left + right
    return -1


def is_correct_braket_pair(p):
    stack = []
    for c in p:
        if stack and stack[-1] == "(" and c == ")":
            stack.pop()
        else:
            stack.append(c)
    return not stack


def solution(p):
    if not p:
        return p

    minimum_index = get_minimum_balanced_braket_index(p)
    u, v = p[:minimum_index], p[minimum_index:]

    if is_correct_braket_pair(u):
        return u + solution(v)

    correct = ""
    correct += "("
    correct += solution(v)
    correct += ")"

    for c in u[1:-1]:
        correct += "(" if c == ")" else ")"
    return correct


p = "()))((()"
print(solution(p))
