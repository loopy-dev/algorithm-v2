from collections import deque

INF = 987654321
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def get_next_pos(sy, sx, i, board):
    y, x = sy, sx

    while True:
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]):
            break

        if board[ny][nx] == "D":
            break

        y, x = ny, nx

    return y, x


def bfs(sy, sx, ey, ex, board):
    q = deque()
    matrix = make_adj(board)
    matrix[sy][sx] = 0
    q.append((sy, sx, 0))

    while q:
        y, x, cnt = q.popleft()

        if board[y][x] == "G":
            continue

        for i in range(4):
            ny, nx = get_next_pos(y, x, i, board)

            if matrix[ny][nx] > cnt + 1:
                matrix[ny][nx] = cnt + 1
                q.append((ny, nx, cnt + 1))

    return matrix[ey][ex] if matrix[ey][ex] < INF else -1


def make_adj(board):
    matrix = []

    for _ in range(len(board)):
        row = []
        for _ in range(len(board[0])):
            row.append(INF)
        matrix.append(row)
    return matrix


def solution(board):
    sy, sx = -1, -1
    ey, ex = -1, -1

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                sy, sx = i, j
            elif board[i][j] == "G":
                ey, ex = i, j

    ret = bfs(sy, sx, ey, ex, board)
    return ret


arr = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(arr))
