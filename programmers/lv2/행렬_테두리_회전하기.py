from collections import deque


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def get_matrix_border(self, r1, c1, r2, c2):
        ret = []
        for x in range(c1, c2):
            ret.append(self.matrix[r1][x])
        for y in range(r1, r2):
            ret.append(self.matrix[y][c2])
        for x in range(c2, c1, -1):
            ret.append(self.matrix[r2][x])
        for y in range(r2, r1, -1):
            ret.append(self.matrix[y][c1])
        return ret

    def set_matrix_border(self, r1, c1, r2, c2, q):
        """
        q: deque
        """
        for x in range(c1, c2):
            self.matrix[r1][x] = q.popleft()
        for y in range(r1, r2):
            self.matrix[y][c2] = q.popleft()
        for x in range(c2, c1, -1):
            self.matrix[r2][x] = q.popleft()
        for y in range(r2, r1, -1):
            self.matrix[y][c1] = q.popleft()

    def __str__(self):
        return str(self.matrix)


def solution(rows, columns, queries):
    matrix = Matrix(
        [[1 + i + j * columns for i in range(columns)] for j in range(rows)]
    )

    answer = []
    for query in queries:
        r1, c1, r2, c2 = query
        arr = matrix.get_matrix_border(r1 - 1, c1 - 1, r2 - 1, c2 - 1)

        # append to answer array
        sorted_arr = sorted(arr)
        answer.append(sorted_arr[0])

        # rotate
        q = deque(arr)
        q.rotate(1)
        matrix.set_matrix_border(r1 - 1, c1 - 1, r2 - 1, c2 - 1, q)

    return answer


rows = 6
columns = 3
queries = [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]
print(solution(rows, columns, queries))
