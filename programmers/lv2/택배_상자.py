def solution(order):
    stack = []
    box = 1
    count = 0
    idx = 0

    while box <= len(order):
        stack.append(box)
        box += 1

        while stack and stack[-1] == order[idx]:
                stack.pop()
                count += 1
                idx += 1

    return count


order = [4, 3, 1, 2, 5]
print(solution(order))
