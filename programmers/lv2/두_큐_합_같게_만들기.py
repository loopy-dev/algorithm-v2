from collections import deque


def pop_and_push(pop, push):
    p = pop.popleft()
    push.append(p)
    return p


# s1 > s2 -> queue1.pop() and quque2.push()
# s1 < s2 -> queue2.pop() and queue1.push()
def solution(queue1, queue2):
    s1 = sum(queue1)
    s2 = sum(queue2)
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)

    while s1 != s2:

        if s1 > s2:
            p = pop_and_push(q1, q2)
            s1 -= p
            s2 += p

        else:
            p = pop_and_push(q2, q1)
            s2 -= p
            s1 += p

        answer += 1

        if answer >= 600000:
            return -1

    return answer

queue1 = [1, 1]
queue2 = [1, 5]
print(solution(queue1, queue2))
