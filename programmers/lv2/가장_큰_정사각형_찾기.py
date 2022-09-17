def solution(board):
    max_value = 0
    dp = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                continue

            dp[i][j] += board[i][j]
            dp[i][j] += min(
                dp[i - 1][j] if i - 1 >= 0 else 0,
                dp[i][j - 1] if j - 1 >= 0 else 0,
                dp[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0,
            )
            max_value = max(max_value, dp[i][j])

    return max_value**2


board = [[0, 1, 1, 1]]
print(solution(board))
