# 수열은 비 내림차순
# 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함하는 부분 수열
# 부분 수열의 합은 k여야 함
# 합이 k인 부분 수열이 여러 개인 경우 길이가 가장 짧은 수열
# 길이가 짧은 수열이 여러 개인 경우 시작 인덱스가 작은 수열을 찾는다.
# 각 원소는 모두 0보다 큰 정수이므로 k보다 큰 경우 left를 하나 빼는 식으로 운영
# 투포인터로 접근 시 시간초과 발생

INF = 987654321


def meet_condition(sequence, left, right, k):
    s = 0
    for i in range(left, right + 1):
        s += sequence[i]

    if s == k:
        return 0

    if s < k:
        return 1

    return 2


def solution(sequence, k):
    answer = [-INF, INF]
    left = 0
    right = 0

    while right < len(sequence):
        result = meet_condition(sequence, left, right, k)  # result will be 0, 1, 2

        # if meet condition: return left and right
        if result == 0:
            # check previous left, right
            # change answer if abs(right - left) is smaller than abs(previous_right - previous_left)
            if abs(right - left) < abs(answer[1] - answer[0]):
                answer = [left, right]
                continue

            if abs(right - left) == abs(answer[1] - answer[0]) and answer[0] > left:
                answer = [left, right]

        # if sum(left:right) is smaller than k, right += 1
        if result == 1:
            right += 1
            continue

        # if sum(left:right) is bigger than k, left += 1, right = left + 1
        left += 1

    return answer


arr = [2, 2, 2, 2, 2]
k = 6
print(solution(arr, k))
