"""
Flipping bits(비트 뒤집기?)
You will be given a list of 32 bit unsigned integers. 
Flip all the bits ( and ) and return the result as an unsigned integer.
"""
"""
해결 방법
비트를 뒤집는 연산자는 NOT 연산자를 사용할 수 있다.

1. 숫자를 이진수처럼 생각하고, 비트의 자리수대로 탐색을 한다.
2. ~ 연산자를 이용하여 비트를 뒤집는다.
3. 모든 비트를 뒤집었으면 값을 반환한다.
32비트이기 때문에 비트의 자리수는 항상 32자리수로 고정한다.

1-1. 탐색은 비트 연산자 &를 이용한다.
example:

100001
비트를 뒤집으면 보수가 되므로, 해당 수의 보수를 구하면 된다.
"""


def flippingBits(n):
    # iterate bits from 0 to 32
    counter = 0

    for i in range(32):
        current_bit = n & (1 << i)

        # 현재 자리가 0일 경우 자리수를 더한다.
        if not current_bit:
            counter += 1 << i

    return counter
