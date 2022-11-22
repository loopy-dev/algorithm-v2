"""
flip 하는 것은, 특정 위치에 고정적으로만 위치할 수 있다는 성질을 찾아내는 것이 중요하다.
"""


def flipping_matrix(matrix):
    value = 0
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row // 2):
        for j in range(col // 2):
            max_value = max(
                matrix[i][j],
                matrix[row - i - 1][j],
                matrix[i][col - j - 1],
                matrix[row - i - 1][col - j - 1],
            )
            value += max_value

    return value


matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
print(flipping_matrix(matrix))
