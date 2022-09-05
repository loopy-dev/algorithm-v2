from itertools import permutations
import math


def is_prime_number(number):
    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def solution(numbers):
    s = set()

    for i in range(1, len(numbers) + 1):
        p = permutations(list(numbers), i)
        for c in p:
            s.add(int("".join(list(c))))

    return len(list(filter(lambda x: is_prime_number(x), list(s))))


numbers = "011"
print(solution(numbers))
