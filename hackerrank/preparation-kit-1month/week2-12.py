"""
Counter game

2의 제곱수인지 확인하고 맞다면 2로 나눈다.
그렇지 않다면 그 다음으로 작은 2의 제곱수를 찾고 그 수를 뺀다.
1로 만드는 사람이 이긴다.
Louise가 먼저 시작한다. 
"""
"""
제곱 수를 찾는 방법
n & (n - 1) == 0일 경우
example:
4 = 100
3 = 011이므로 항상 0이 성립한다.



6 -> 2 -> 1
louise richard
"""
import sys
import math

sys.setrecursionlimit(10000000)


def is_power_of_2(n):
    return (n & (n - 1)) == 0


def get_substract_value(n):
    return int(n - 2 ** (math.log10(n) // math.log10(2)))


def play(n):
    if n == 1:
        return True

    # if n is not power of 2
    if not is_power_of_2(n):
        nxt = get_substract_value(n)
        return not play(nxt)

    # else divide n by 2
    return not play(n // 2)


def counterGame(n):
    return "Richard" if play(n) else "Louise"


n = 1560834904
print(counterGame(n))
