"""
Permuting Two Arrays
n개의 요소를 갖고 있는 두 개의 배열 A, B가 있다. 이 둘을 섞어 A', B'를 만드려고 한다.
A'[i] + B'[i] >= k를 만족해야 한다.

example:
A = [0, 1]
B = [0, 2]
k = 1

A' = [1, 0]
B' = [0, 2]
라면 모든 i에 대해 A'[i] + B'[i] >= 1이 성립한다. 이 경우, YES를 반환하고
그렇지 않다면 NO를 반환한다.
"""
"""
접근 방법
1. permutation을 한다. 배열 1개만 permutation을 진행한다.
2. permutation 후 비교하여 조건을 만족하는지 확인한다.
3. 값을 도출한다.

그러나 1000개를 permutation할 수는 없다. permutation을 하고, 더하는 과정에서
시간 절약이 필요하다.

가장 큰 값과 가장 작은 값을 더해서 k를 넘지 못한다면 다른 값도 넘길 수 없다는 뜻이다.
따라서 배열 1개는 오름차순으로, 나머지는 내림차순으로 정렬하고 두 값을 더한다.
"""


def check(k, arr1, arr2):
    length = len(arr1)

    for i in range(length):
        if arr1[i] + arr2[i] < k:
            return False

    return True


def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)

    return "YES" if check(k, A, B) else "NO"


a = [2, 1, 3]
b = [7, 8, 9]
k = 5
print(twoArrays(k, a, b))
