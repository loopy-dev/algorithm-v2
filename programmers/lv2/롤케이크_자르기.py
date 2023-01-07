"""
롤케이크 자르기

1. 배열을 앞에서부터 순회하면서 경우의 수를 구한다.
1-1. set에 없다면 이전 배열에 + 1을, 그렇지 않다면 이전 배열의 값을 복사한다.
2. 배열을 뒤에서부터 순회하면서 경우의 수를 구한다.
3. 배열을 순회하면서 앞에서 순회한 값과 뒤에서 순회한 값을 더한다.
"""


def solution(topping):
    answer = 0
    p1 = set()
    p2 = set()
    people1 = [0] * len(topping)
    people2 = [0] * len(topping)

    # people1
    p1.add(topping[0])
    people1[0] = 1
    for i in range(1, len(topping)):
        people1[i] = people1[i - 1]

        if topping[i] not in p1:
            p1.add(topping[i])
            people1[i] += 1

    # people2
    p2.add(topping[-1])
    people2[-1] = 1
    for i in range(len(topping) - 2, -1, -1):
        people2[i] = people2[i + 1]

        if topping[i] not in p2:
            p2.add(topping[i])
            people2[i] += 1

    # check
    for i in range(len(topping) - 1):
        if people1[i] == people2[i + 1]:
            answer += 1

    return answer


topping = [1, 2, 3, 1, 4]
print(solution(topping))
