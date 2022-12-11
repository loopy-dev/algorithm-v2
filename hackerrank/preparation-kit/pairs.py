"""
Given an array of integers and a target value, determine the number of pairs
of array elements that have a DIFFERENCE EQUAL TO THE TARGET VALUE.
"""
"""
가장 원초적으로 접근하기
배열을 순회하는 두 개의 포인터
두 번의 반복문을 진행하여 값의 차이가 k인 경우를 찾기

2. 배열의 숫자의 개수와 상관없이 쌍만 구하면 되기 때문에, boolean 배열을 이용하여
두 pair간 숫자가 존재하는지 확인
n - k범위까지 한 번의 순회로 확인이 가능

arr[i]의 범위가 2 ** 31까지 이므로 배열을 사용할 경우 메모리 에러가 발생

"""
"""
이전 방법

def pairs(k, arr):
    max_value = max(arr)
    counts = [False] * (max_value + 1)
    count = 0

    # check if value exists
    for i in range(len(arr)):
        number = arr[i]
        counts[number] = True

    # get pairs count
    for i in range(1, len(counts) - k):
        if counts[i] and counts[i + k]:
            count += 1

    return count

"""
"""
개선 방법

set을 이용하여 O(1)의 시간복잡도로 접근할 수 있도록 함
카운팅 배열을 만드는 것이 아닌, 배열을 정렬 후 + k 한 값이 set에 존재하는지 확인하므로서
시간 복잡도 및 공간 복잡도 개선 가능
"""

def pairs(k, arr):
    arr.sort()
    s = set()
    count = 0

    # check if value exists
    for i in range(len(arr)):
        s.add(arr[i])

    # get pairs count
    for i in range(len(arr)):
        if arr[i] + k in s:
            count += 1

    return count

k = 2
arr = [1, 5, 3, 4, 2]
print(pairs(k, arr))
