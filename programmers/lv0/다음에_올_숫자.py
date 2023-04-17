# 등차수열 - 두 수의 차가 일정
# 등비수열 - 두 수의 비가 일정
# 등차 수열과 등비 수열 중 하나가 아닌 경우는 없다.
# 적어도 3개의 수가 나오므로 앞의 3 수를 확인한다.
# 0번과 1번 차이 확인, 1번과 2번 차이 확인
# 차이 동일 -> 등차수열이므로 등차수열 공식 적용
# 그렇지 않다면 등비수열이므로 등비수열 공식 적용
# 단 공비가 -일 경우에 대하여 주의해야 함


def is_arithmetic_sequence(a, b, c):
    return abs(a - b) == abs(b - c)


def solution(seq):
    if is_arithmetic_sequence(seq[0], seq[1], seq[2]):
        diff = seq[1] - seq[0]
        return seq[-1] + diff
    ratio = seq[1] // seq[0]
    return seq[-1] * ratio


# seq = [1, 2, 3, 4]
seq = [2, 4, 8]
print(solution(seq))
