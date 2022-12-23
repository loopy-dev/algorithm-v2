"""
Flipping the matrix

몇 번이고 뒤집을 수 있기 때문에 해당 위치에 올 수 있는 가장 작은 값을 찾는다.
example:
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

arr[0][0]: max(arr[0][0], arr[0][3], arr[3][0], arr[3][3])
일반화:
arr[i][j]: max(arr[i][j], arr[i][2n - 1 - j], arr[2n - 1 - i][j], arr[2n - 1 - i][2n - 1 - j]), i < n && j < n
"""


def flippingMatrix(matrix):
    s = 0
    half = len(matrix) // 2
    length = len(matrix)

    # iterate matrix and get max value
    for i in range(half):
        for j in range(half):
            s += max(
                matrix[i][j],
                matrix[i][length - 1 - j],
                matrix[length - 1 - i][j],
                matrix[length - 1 - i][length - 1 - j],
            )

    return s


matrix = [[1, 2], [3, 4]]
print(flippingMatrix(matrix))
