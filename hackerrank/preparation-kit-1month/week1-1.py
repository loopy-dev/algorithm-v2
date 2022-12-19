"""
Plus Minus
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
"""


def print6f(number):
    print(f"{number:.6f}")


def plusMinus(arr):
    """
    1. 배열을 순회하면서 plus의 개수, minus의 개수, zero의 개수를 센다.
    2. 이를 총 배열 요소의 개수로 나누고, 6의자리까지 나타낸다.
    3. 만약 작은 숫자 순서대로 정렬한다면, 모든 배열을 순회할 필요 없이 minus, 0의 개수에서 빼서 plus를 표현할 수도 있다.
    정렬에는 O(n * log(n))의 시간 복잡도가 필요하므로 순차적으로 계산하는 것이 더 빠르다.
    """
    total = len(arr)
    negative, zero, positive = 0, 0, 0

    for c in arr:
        if c < 0:
            negative += 1

        elif c == 0:
            zero += 1

        else:
            positive += 1

    print6f(positive / total)
    print6f(negative / total)
    print6f(zero / total)


arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)
