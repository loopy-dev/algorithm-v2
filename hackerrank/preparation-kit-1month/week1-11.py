"""
Subarray division 1
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
Lily decides to share a contiguous segment of the bar selected such that:
인접한 요소들을 공유한다.

segement의 길이가 Ron의 생월과 동일하다.
정수의 합이 그의 생일과 동일하다.
경우의 수를 구해야 한다.
example:
s = [2, 2, 1, 3, 2]
d = 4
m = 2 라고 했을 때,
[2, 2] 또는 [1, 3]이 가능한 경우일 수 있다.
"""
"""
무식한 방법으로 해결하기
1. 우선 배열을 2씩 자른다.
2. 자른 배열의 합을 더한다.
3. 그 합이 d가 될 수 있는지 확인하고, 가능하다면 경우의 수를 1 더한다.

최적화하기
0부터 n까지의 부분 합을 구한다.
인덱스를 이용하여 더한다.
배열을 1번 순회하면서 가능한 조건이 존재하는지 확인한다.

인접한 배열의 합은 부분합을 통해 구할 수 있으며, 더 나아가 2차원으로 확장도 가능하다.
"""


def get_partial_sum(arr):
    s = 0
    ret = []
    ret.append(s)

    for i in range(len(arr)):
        s += arr[i]
        ret.append(s)

    return ret


def birthday(s, d, m):
    p_sum = get_partial_sum(s)
    count = 0

    for i in range(len(p_sum) - m):
        if p_sum[i + m] - p_sum[i] == d:
            count += 1

    return count


s = [2, 2, 1, 3, 2]
d = 4
m = 2
print(birthday(s, d, m))
