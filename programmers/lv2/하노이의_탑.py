class Hanoi:
    def __init__(self):
        self.answer = []

    def hanoi(self, _from, _to, _via, n):
        if n == 1:
            self.answer.append([_from, _to])
            return

        self.hanoi(_from, _via, _to, n - 1)
        self.answer.append([_from, _to])
        self.hanoi(_via, _to, _from, n - 1)


def solution(n):
    hanoi = Hanoi()
    hanoi.hanoi(1, 3, 2, n)
    return hanoi.answer


n = 3
print(solution(n))
