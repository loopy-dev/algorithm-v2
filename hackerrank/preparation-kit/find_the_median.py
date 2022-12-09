def findMedian(arr):
    arr.sort()
    mid = len(arr) // 2
    return arr[mid]


arr = [0, 1, 2, 4, 6, 5, 3]

print(findMedian(arr))