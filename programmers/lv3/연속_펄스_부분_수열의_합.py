"""
어떤 수열의 연속 부분 수열에 연속 펄스 부분 수열을 곱하여
가장 큰 합을 반환하기

1. 연속된 부분 수열을 탐색
2. 연속된 부분 수열에서 [-1, 1, -1, 1], [1, -1, 1, -1] 순서대로 계산
최댓값 구하기
"""

INF = int(1e12)


def create_sequence(sequence, flag):
    ret = []
    check = 1

    if flag:
        check = 1
    else:
        check = -1

    for i in range(len(sequence)):
        if i % 2 == 0:
            ret.append(sequence[i] * check)
        else:
            ret.append(sequence[i] * -check)

    return ret


def create_partial_sum_sequence(sequence):
    ret = []
    s = 0
    for i in range(len(sequence)):
        ret.append(s)
        s += sequence[i]
    ret.append(s)

    return ret


def get_max_sum(sequence):
    max_value = -INF
    min_value = INF
    for i in range(len(sequence)):
        max_value = max(max_value, sequence[i])
        min_value = min(min_value, sequence[i])

    return max_value - min_value


def solution(sequence):
    answer = -INF
    seq1 = create_sequence(sequence, True)
    seq2 = create_sequence(sequence, False)

    psum1 = create_partial_sum_sequence(seq1)
    psum2 = create_partial_sum_sequence(seq2)

    answer = max(answer, get_max_sum(psum1), get_max_sum(psum2))

    return answer


sequence = [2, 3, -6, 1, 3, -1, 2, 4]
print(solution(sequence))
