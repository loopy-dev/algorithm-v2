"""
Recursive Digit Sum

재귀적으로 1자리 수가 남을 때까지 해결하기
"""
"""
1. 재귀적으로 계산한다.
2. 총 자리수가 10만이고 1만번 곱할 수 있기 때문에 단순한 방법보다 최적화가 필요하다.
3. 반복되는 숫자이기 때문에 우선 하나에 대해서 값을 구한 뒤 해당 값을 곱하고 다시 반복한다면
재귀 깊이 내에 해결할 수 있다.
"""


def get_super_digit(digit):
    # if x has only 1 digit, then its super digit is x
    if len(digit) <= 1:
        return digit

    s = 0
    for c in digit:
        s += int(c)

    return get_super_digit(str(s))


def superDigit(n, k):
    # Write your code here
    s = int(get_super_digit(n)) * k
    return get_super_digit(str(s))
