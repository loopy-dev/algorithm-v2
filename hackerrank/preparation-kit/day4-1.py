"""
Grid Challenge
Given a square grid of characters in the range ascii[a-z], 
rearrange elements of each row alphabetically, ascending. 
Determine if the columns are also in ascending alphabetical order, 
top to bottom. Return YES if they are or NO if they are not.
"""
"""
1. 모든 row에 대해서 sort를 한다
2. col에 대해 오름차순으로 정렬이 되어 있는지 확인한다.
"""


def gridChallenge(grid):
    # create matrix
    matrix = []
    for i in range(len(grid)):
        row = []

        for j in range(len(grid[0])):
            row.append(grid[i][j])

        row.sort()
        matrix.append(row)

    # check col if col is arranged in ascending
    for j in range(len(matrix[0])):
        col = []

        for i in range(len(matrix)):
            col.append(matrix[i][j])

        if col != sorted(col):
            return "NO"

    return "YES"
