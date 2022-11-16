#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
"""

# 꼭 연속된 합일 필요는 없다
# 길이가 5로 고정된 배열이므로, min, max 함수를 이용하여 최솟값, 최댓값을 찾는다.
# 총 합에서 최댓값을 빼면 최소합이 되고, 최솟값을 빼면 최대 합이 될 것이다.

def miniMaxSum(arr):
    # Write your code here
    sum_value = sum(arr)
    min_value = min(arr)
    max_value = max(arr)

    print(sum_value - max_value, sum_value - min_value)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
