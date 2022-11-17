#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

"""
하나를 제외하면, 무조건 두 개 존재하므로, boolean 자료형을 이용하여 관리를 하는 것이 좋을 듯 하다.
ex) 첫 번째로 값을 만나면 True, 두 번째로 값을 만나면 False
인덱스를 만난 숫자로 생각하면 좋을 듯 하다. 왜냐하면 1부터 100사이의 값을 가지고 있기 때문에, 배열 자료구조로
관리 하더라도 메모리상에 문제가 발생하지 않는다.
"""

def lonelyinteger(a):
    # Write your code here
    arr = [False] * 101
    ret = 0
    
    for i in a:
        arr[i] = not arr[i]
    
    for i in range(len(arr)):
        if arr[i]:
            ret = i
            break
    
    return ret



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
