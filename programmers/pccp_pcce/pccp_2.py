# pccp 모의고사 1번 - 체육대회


def solution(ability):
    s = set()
    answer_set = set()

    def backtrack(idx, current):
        if idx == len(ability[0]):
            answer_set.add(current)
            return

        for i in range(len(ability)):
            if i in s:
                continue
            s.add(i)
            backtrack(idx + 1, current + ability[i][idx])
            s.remove(i)

    backtrack(0, 0)
    return max(list(answer_set))


ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
print(solution(ability))
