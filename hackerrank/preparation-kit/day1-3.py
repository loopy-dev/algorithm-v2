#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
"""

# 1. 12:00:00AM ~ 11:59:59AM -> 00:00:00 ~ 11:59:59
# 2. 12:00:00PM ~ 11:59:59PM -> 12:00:00 ~ 23:59:59
# 12 % 12 = 0 일 경우 && AM: 0으로 변환
# 12 % 12 = 0 && PM: 0 더하기

def timeConversion(s):
    time = list(map(int, s[:-2].split(':')))
    f = s[-2:]

    time[0] %= 12
    
    if f == 'PM':
        time[0] += 12

    return ":".join(list(map(lambda x: format(x, '02'), time)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
