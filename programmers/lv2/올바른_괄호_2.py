def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return False
            if stack[-1] == '(':
                stack.pop()
    if stack:
        return False
    return True


s = "(())()"
print(solution(s))
