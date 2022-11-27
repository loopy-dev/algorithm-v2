"""
Balanced brakets
There are three types of matched pairs of brackets: [], {}, and ().
밸런스인지 아닌지 확인하기
"""
"""
스택을 이용하여 pair가 나오면 stack.pop하고, 그렇지 않으면 stack.push 한다.
"""


def isBalanced(s):
    # Write your code here
    stack = []

    for c in s:
        if stack:
            if stack[-1] == "(" and c == ")":
                stack.pop()

            elif stack[-1] == "{" and c == "}":
                stack.pop()

            elif stack[-1] == "[" and c == "]":
                stack.pop()

            else:
                stack.append(c)

        else:
            stack.append(c)

    if stack:
        return "NO"
    return "YES"
