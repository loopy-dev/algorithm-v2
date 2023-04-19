# 최소한의 객실만을 사용
# 퇴실 시간을 기준으로 10분간 청소후 입장 가능
# 예약시간이 주어질 때 필요한 최소 객실 수
# 종료 시간에 10분 추가하기


def parse_time(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)


def solution(book_time):
    timeline = [0] * (24 * 60 + 100)
    books = list(map(lambda x: [parse_time(x[0]), parse_time(x[1]) + 10], book_time))
    answer = 0

    for start_time, end_time in books:
        timeline[start_time] += 1
        timeline[end_time] -= 1

    # timeline 만들기
    for i in range(1, len(timeline)):
        timeline[i] += timeline[i - 1]

    for i in range(len(timeline)):
        answer = max(answer, timeline[i])

    return answer


book_time = [
    ["15:00", "17:00"],
    ["16:40", "18:20"],
    ["14:20", "15:20"],
    ["14:10", "19:20"],
    ["18:20", "21:20"],
]
print(solution(book_time))
