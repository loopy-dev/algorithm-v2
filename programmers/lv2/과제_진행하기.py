# 과제는 시작하기로 한 시간이 되면 시작
# 새로운 과제를 시작한 시간이 되면 기존에 진행중인 과제를 멈추고 새로운 과제를 시작
# 진행중이던 과제를 끝내고 이전에 진행하던 과제가 있다면 멈춰둔 과제를 이어서 진행
# 과제를 끝냈을 때 새로 시작해야 하는 과제와 잠시 멈춰둔 과제가 모두 있다면 새로운 과제먼저
# 멈춰둔 과제가 여러 개라면 가장 최근에 멈춘 과제부터 시작
# 가장 최근에 멈춘 과제 -> stack 활용을 유추할 수 있다.
# 60 * 24 = 1440으로 충분히 배열을 이용하여 해결할 수도 있음
# 단 뭔가 누적되는 그림은 아니기 때문에 누적해서 뭔가 해결하는 그림은 아닌듯?


def t_to_m(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)


# plan: [name, start, play_time]
def solution(plans):
    stack = []
    answer = []

    # start_time, end_time을 모두 분 단위로 바꾸기
    arr = []
    for i in range(len(plans)):
        name, start_time, play_time = plans[i]
        start = t_to_m(start_time)
        pt = int(play_time)
        arr.append([name, start, pt])

    # start_time 오름차순으로 정렬
    arr.sort(key=lambda x: x[1])

    # stack에 삽입
    stack.append([arr[0][0], arr[0][2]])
    t = arr[0][1]

    for i in range(1, len(plans)):
        current_name, current_st, current_pt = arr[i]

        while stack:
            prev_name, prev_pt = stack.pop()

            if t + prev_pt <= current_st:
                answer.append(prev_name)
                t += prev_pt
                continue

            stack.append([prev_name, prev_pt - (current_st - t)])
            break

        t = current_st
        stack.append([current_name, current_pt])

    # 마지막에 처리할 부분
    while stack:
        current_name, current_pt = stack.pop()
        answer.append(current_name)
        t += current_pt

    return answer


plans = [
    ["science", "12:40", "50"],
    ["music", "12:20", "40"],
    ["history", "14:00", "30"],
    ["computer", "12:30", "100"],
]
print(solution(plans))
