import math


def solution(h1, m1, s1, h2, m2, s2):
    # h1,m1,s1을 숫자로 변경한다.
    answer = 0
    start_time = time_format(h1, m1, s1)
    end_time = time_format(h2, m2, s2)
    cycle = 2 * math.pi
    cycle_s = cycle / 60
    cycle_m = cycle / (60 * 60)
    cycle_h = cycle / (60 * 60 * 12)

    for t in range(start_time, end_time):
        x1 = get_sin_value(cycle_s, t % 60)
        x2 = get_sin_value(cycle_s, (t + 1) % 60)
        y1 = get_sin_value(cycle_m, t % (60 * 60))
        y2 = get_sin_value(cycle_m, (t + 1) % (60 * 60))
        z1 = get_sin_value(cycle_h, (t) % (12 * 60 * 60))
        z2 = get_sin_value(cycle_h, (t + 1) % (12 * 60 * 60))

        if is_collapsed(x1, y1, x2, y2):
            answer += 1
        if is_collapsed(x1, z1, x2, z2):
            answer += 1
        if is_collapsed(y1, z1, y2, z2):
            answer -= 1

    return answer


def time_format(h, m, s):
    return h * 3600 + m * 60 + s


def get_sin_value(cycle, time):
    return math.sin(cycle * time)


def is_collapsed(x1, y1, x2, y2):
    a2 = x2 - y2
    a1 = x1 - y1
    return a2 >= 0 and a1 <= 0


h1 = 11
m1 = 59
s1 = 59
h2 = 12
m2 = 0
s2 = 0
print(solution(h1, m1, s1, h2, m2, s2))
