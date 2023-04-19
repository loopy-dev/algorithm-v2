# 게임을 했을 때 나올 수 있는 상황이라면 1
# 그렇지 않다면 0을 반환
s = set()


def game_over(board):
    # 가로, 세로, 대각선으로 완성되었다.
    # 가로로 완성됨
    for i in range(3):
        if board[i][0] != "." and board[i][0] == board[i][1] == board[i][2]:
            return True

    # 세로로 완성됨
    for j in range(3):
        if board[0][j] != "." and board[0][j] == board[1][j] == board[2][j]:
            return True

    # 대각선으로 완성됨
    if board[0][0] != "." and board[0][0] == board[1][1] == board[2][2]:
        return True

    # 대각선으로 완성됨
    if board[0][2] != "." and board[0][2] == board[1][1] == board[2][0]:
        return True

    # 더 이상 둘 공간이 없다.
    for i in range(3):
        for j in range(3):
            if board[i][j] == ".":
                return False

    return True


def backtrack(board, current):
    # 진행 중인 상황을 추가
    result = ""
    for i in range(3):
        for j in range(3):
            result += board[i][j]

    if result in s:
        return

    s.add(result)

    # 더 이상 게임을 진행할 수 없다면
    # set에 추가
    if game_over(board):
        return

    for i in range(3):
        for j in range(3):
            if board[i][j] != ".":
                continue

            board[i][j] = current
            backtrack(board, "O" if current == "X" else "X")
            board[i][j] = "."


def solution(board):
    backtrack([[".", ".", "."], [".", ".", "."], [".", ".", "."]], "O")
    return 1 if "".join(board) in s else 0


board = ["...", "...", "..."]
print(solution(board))
