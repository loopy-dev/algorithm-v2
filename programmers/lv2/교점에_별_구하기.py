INF = int(1e15)


def isinteger(number):
    return number - int(number) == 0


def find_the_solution(line1, line2):
    """
    두 직선의 교차점을 구하는 함수
    """
    a, b, e = line1
    c, d, f = line2
    # 문제에서 ad - bc != 0임을 보장한다.
    matrix1 = get_inverse_matrix([[a, b], [c, d]])
    matrix2 = [[-e], [-f]]
    ret = multiply_matrix(matrix1, matrix2)
    return [ret[0][0], ret[1][0]]  # [x, y]


def get_inverse_matrix(matrix):
    """
    2차원 행렬의 역행렬을 구하는 함수
    """
    a, b = matrix[0]
    c, d = matrix[1]
    discriminant = a * d - b * c
    return [
        [d / discriminant, -b / discriminant],
        [-c / discriminant, a / discriminant],
    ]


def multiply_matrix(matrix1, matrix2):
    """
    곱할 수 있는 두 행렬의 곱을 구하는 함수
    """
    row_of_new_matrix = len(matrix1)
    col_of_new_matrix = len(matrix2[0])
    common = len(matrix1[0])

    answer = []
    for i in range(row_of_new_matrix):
        row = []
        for j in range(col_of_new_matrix):
            temp = 0
            for k in range(common):
                temp += matrix1[i][k] * matrix2[k][j]
            row.append(temp)
        answer.append(row)

    return answer


def find_point(line1, line2):
    a, b, e = line1
    c, d, f = line2

    mod = a * d - b * c

    return [(b * f - e * d) / mod, (e * c - a * f) / mod]


def solution(line):
    min_y, min_x = INF, INF
    max_y, max_x = -INF, -INF
    intersections = []
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            a, b, _ = line[i]
            c, d, _ = line[j]

            if not a * d - b * c:
                continue

            x, y = find_point(line[i], line[j])

            if isinteger(x) and isinteger(y):
                intersections.append((int(x), -int(y)))
                min_y = min(min_y, -int(y))
                min_x = min(min_x, int(x))
                max_y = max(max_y, -int(y))
                max_x = max(max_x, int(x))

    # min_y, min_x를 offset으로 설정하여 새로운 배열을 만든다.
    board = [["." for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for x, y in intersections:
        board[y - min_y][x - min_x] = "*"
    return ["".join(board[i]) for i in range(len(board))]


line = [[2, -1, 2], [2, -1, -2], [-2, -1, 2], [-2, -1, -2]]
print("\n".join(solution(line)))
