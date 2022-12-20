"""
Lonely Integer
Given an array of integers, where all elements but one occur twice, find the unique element.
배열 내의 요소가 한 개인 요소를 반환하면 된다.
"""
"""
풀이 방법 1

마지막에 요소가 나올 수 있기 때문에 배열 끝까지 순회가 필요하다.
1. 모든 배열을 순회한다.
2. 배열을 순회하면서 요소가 몇 번 나왔는지 확인한다. 이를 카운팅 배열 또는 딕셔너리에 저장한다.
3. 딕셔너리에 요소의 개수가 1인 것을 필터링하여 반환한다.
시간 복잡도는 O(A + B)
A: input 배열의 길이
B: 딕셔너리의 길이

풀이 방법 2

bisect를 이용하여 문제를 해결할 수도 있을듯 하다.
1. 배열을 정렬한다.
2. 정렬된 배열을 set 자료구조에 삽입하여, key가 무엇이 있는지 확인한다.
3. bisect를 통해 요소가 한 개만 존재하면 반환한다.
"""
from bisect import bisect_left, bisect_right


def lonelyinteger(a):
    # key를 set에 저장
    s = set(a)

    # bisect 알고리즘을 사용하기 위해서는 정렬되어 있어야 한다.
    a.sort()

    for key in s:
        if bisect_right(a, key) - bisect_left(a, key) == 1:
            return key

    return -1
