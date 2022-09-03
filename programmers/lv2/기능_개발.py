from collections import deque


def solution(progresses, speeds):
    q = deque(progresses)
    s = deque(speeds)
    answer = []

    while q:
        count = 0
        for i in range(len(q)):
            q[i] += s[i]

        while q and q[0] >= 100:
            q.popleft()
            s.popleft()
            count += 1

        if count > 0:
            answer.append(count)

    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))
