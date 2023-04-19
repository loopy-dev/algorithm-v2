# 내 공을 좌표를 확장하여 반대편으로 절댓값을 취한 후 최솟값을 구한다.
# 공이 가려는 방향과 같은 방향에 목표가 있다면 원쿠션이 불가능함에 주의한다.
# 총 4번 반복하면 된다.
INF = 987654321


def is_same_direction(beforeY, afterY, ballY, beforeX, afterX, ballX):
    return (beforeY <= ballY <= afterY or beforeY >= ballY >= afterY) and (
        beforeX <= ballX <= afterX or beforeX >= ballX >= afterX
    )


def get_value(m, n, startX, startY, ball):
    x, y = ball
    a = (2 * n - startY - y) ** 2 + (startX - x) ** 2
    b = (startY + y) ** 2 + (startX - x) ** 2
    c = (startY - y) ** 2 + (x + startX) ** 2
    d = (startY - y) ** 2 + (2 * m - startX - x) ** 2

    return min(
        [
            a
            if not is_same_direction(startY, 2 * n - startY, y, startX, startX, x)
            else INF,
            b if not is_same_direction(startY, -startY, y, startX, startX, x) else INF,
            c if not is_same_direction(startY, startY, y, startX, -startX, x) else INF,
            d
            if not is_same_direction(startY, startY, y, startX, 2 * m - startX, x)
            else INF,
        ]
    )


def solution(m, n, startX, startY, balls):
    answer = []

    for ball in balls:
        answer.append(get_value(m, n, startX, startY, ball))
    return answer


m = 10
n = 10
startX = 3
startY = 7
balls = [[7, 7], [2, 7], [7, 3]]
print(solution(m, n, startX, startY, balls))
