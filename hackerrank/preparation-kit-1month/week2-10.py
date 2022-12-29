"""
Sherlock and Array

어떤 배열이 주어졌을 때, 특정 원소를 기준으로 왼쪽과 오른쪽이 합이 동일할 수 있다면 YES
그렇지 않으면 NO를 출력하기
"""
"""
1. left = arr[:mid]
2. target = arr[mid]
3. right = sum(arr) - target - left
으로 구할 수 있음

탐색 범위는? 마지막 요소 인덱스까지 탐색할 것
1. 배열을 순회하면서 left, target, right을 구한다.
2. target을 제외한 나머지 값이 동일하다면 true, 그렇지 않다면 false를 반환
"""


def balancedSums(arr):
    return "YES" if is_balanced(arr) else "NO"


def is_balanced(arr):
    left = 0
    s = sum(arr)

    for i in range(len(arr)):
        target = arr[i]
        right = s - target - left

        if left == right:
            print(target)
            return True

        left += target

    return False
