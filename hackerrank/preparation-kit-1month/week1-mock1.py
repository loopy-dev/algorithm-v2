"""
find Median
"""


def findMedian(arr):
    # find middle element after sorting
    arr.sort()

    mid = len(arr) // 2

    return arr[mid]
