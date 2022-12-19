"""
Mini-Max sum
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
"""


def miniMaxSum(arr):
    """
    입력으로 들어오는 배열은 항상 5의 길이를 가지므로, 순회하는 시간은 거의 고려하지 않아도 괜찮다.
    한번에 순회를 통해 찾는 방법은 부분합을 통해 구할 수도 있지만, 5의 길이를 갖기 때문에 의미 없다
    항상 4개의 합이 가장 작거나 큰 것만 사용하기 때문에 정렬을 통해서 구할 수 있겠다.
    정렬을 하면 가장 왼쪽에는 가장 작은 숫자가, 오른쪽에는 가장 큰 숫자가 정렬될 것이다.
    배열의 요소 총 합에서 가장 작은 숫자를 빼면 가장 큰 합이 되고, 가장 큰 숫자를 빼면 가장 작은 합이 될 것이다.
    """
    s = sum(arr)
    arr.sort()
    max_value = s - arr[0]
    min_value = s - arr[-1]

    print(min_value, max_value)


arr = [1, 2, 3, 4, 5]
miniMaxSum(arr)
