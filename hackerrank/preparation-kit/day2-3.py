#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
"""
quick sort보다 더 빠른 알고리즘? cf: O(n * log(n))
counting sort를 구현한다.

배열의 최대 길이: 10 ** 6 (10만)
배열의 요소의 최대 크기는 배열의 최대 길이를 넘지 않는다.
"""

def countingSort(arr):
    # Write your code here
    counts = [0] * 100

    # count element in the arr
    for i in arr:
        counts[i] += 1

    return counts
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
