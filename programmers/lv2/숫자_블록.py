import math


def get_maximum_divisor(n):
    if n == 1:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and n // i <= 10000000:
            return n // i
    return 1


def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        answer.append(get_maximum_divisor(i))
    return answer


begin = 2
end = 10
print(solution(begin, end))
