def solution(arr):
    return compact(0, 0, len(arr), arr)


def compact(start_y, start_x, scale, board):
    answer = [0, 0]
    if scale <= 1:
        if board[start_y][start_x] == 0:
            return [1, 0]

        return [0, 1]

    # 같은 숫자인지 확인하기
    same_number = True
    initial_number = board[start_y][start_x]
    for y in range(start_y, start_y + scale):
        for x in range(start_x, start_x + scale):
            if initial_number != board[y][x]:
                same_number = False
                break

        if not same_number:
            break

    if same_number:
        if initial_number == 0:
            return [1, 0]

        return [0, 1]

    for y in range(start_y, start_y + scale, scale >> 1):
        for x in range(start_x, start_x + scale, scale >> 1):
            ret = compact(y, x, scale >> 1, board)
            answer[0] += ret[0]
            answer[1] += ret[1]

    return answer

arr = [[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]
print(solution(arr))
