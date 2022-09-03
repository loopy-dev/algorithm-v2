def solution(s):
    stack = []
    for c in s:
        if c == ")" and stack and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(c)
    return not bool(len(stack))


s = "(())()"
print(solution(s))
