#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal.
"""

# index of counts arr
PLUS = 0
MINUS = 1
ZERO = 2


def plusMinus(arr):
    # Write your code here
    # 배열을 순회하면서, +, 0, -의 개수를 카운트한다.
    counts = [0, 0, 0]

    for i in range(len(arr)):
        if arr[i] > 0:
            counts[PLUS] += 1

        elif arr[i] == 0:
            counts[ZERO] += 1

        else:
            counts[MINUS] += 1

    # 여섯자리 소수점으로 출력한다.
    print("{:.6f}".format(counts[PLUS] / len(arr)))
    print("{:.6f}".format(counts[MINUS] / len(arr)))
    print("{:.6f}".format(counts[ZERO] / len(arr)))



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
