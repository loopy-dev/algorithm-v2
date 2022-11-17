#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix `arr` is shown below:

"""
n의 범위가 얼마임?
왼쪽부터 순회하면서 left_to_right을 구한다.
오른쪽부터 순회하면서 right_to_left를 구한다.
절댓값을 구한다.

단 한 번의 탐색으로 최적화가 가능하다. -> 인덱스만 잘 관리하면 된다.
"""

def diagonalDifference(arr):
    # Write your code here
    left_to_right = 0
    right_to_left = 0


    for i in range(len(arr)):
        # get left to right sum
        left_to_right += arr[i][i]

        # get right to left sum
        right_to_left += arr[i][len(arr) - i - 1]

    return abs(left_to_right - right_to_left)
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
