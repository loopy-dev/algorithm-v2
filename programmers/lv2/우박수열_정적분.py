def solution(k, ranges):
    pos = solve(k)
    area = [0]
    answer = []

    # 부분합 구하기
    for i in range(1, len(pos)):
        y2 = pos[i]
        y1 = pos[i - 1]
        area.append(area[i - 1] + get_area(y1, y2))

    for s, e in ranges:
        if len(pos) - 1 + e < s:
            answer.append(-1)
            continue

        answer.append(area[len(pos) - 1 + e] - area[s])

    return answer


def get_area(y1, y2):
    return abs(y2 - y1) / 2 + min(y1, y2)


def solve(n):
    if n <= 1:
        return [n]

    answer = [n]

    if n % 2 == 0:
        return answer + solve(n // 2)

    return answer + solve((n * 3) + 1)


k = 5
ranges = [[0, 0], [0, -1], [2, -3], [3, -3]]
print(solution(k, ranges))
