"""
Diagonal Difference (대각선 차이?)
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
절댓값 구하기

제한: 100 * 100
"""
"""
1 2 3
4 5 6
7 8 9

-> 1 + 5 + 9 = 15, 3 + 5 + 7 = 17
|17 - 15| = 2
"""
"""
가장 쉬운 방법:
1. 배열을 순회하면서 왼쪽 위부터 오른쪽 아래의 값을 모두 더한다.
2. 배열을 순회하면서 오른쪽 위부터 왼쪽 아래의 값을 모두 더한다.
3. 둘의 차이를 구한다.

1번의 순회로 시간복잡도 개선하기.
1. left += matrix[i][i] -> left에 더하기
2. right += matrix[len(matrix) - 1 - i][i] -> 왼쪽 아래부터 오른쪽 위 순회 및 더하기
"""


def diagonalDifference(arr):
    left = 0
    right = 0

    # iterate matrix
    for i in range(len(arr)):
        left += arr[i][i]
        right += arr[len(arr) - 1 - i][i]
    
    # get absolute difference
    return abs(right - left)