"""
1. 더하면서 연료 채우기 + 이동할 거리를 빼기
2. 총 연료 + 총 이동 거리가 한번이라도 < 0인 경우가 있다면, 해당 위치에서 출발하는 것은 불가능

최적화
더하면서 연료 채우기, 이동하면서 거리 빼기
이 부분은 반복되는 부분이고 시간 비중이 크므로 최적화가 가능함
최적화 없이도 통과할 수 있었음

"""


def truckTour(petrolpumps):
    s = [0] * len(petrolpumps)

    for i in range(len(petrolpumps)):
        s[i] = petrolpumps[i][0] - petrolpumps[i][1]

    for i in range(len(petrolpumps)):
        if s[i] < 0:
            continue

        flag = True
        partial_sum = 0

        # clockwise
        for j in range(len(petrolpumps)):
            nxt = s[(i + j) % len(petrolpumps)]

            if partial_sum + nxt < 0:
                flag = False
                break

            partial_sum += nxt

        if flag:
            return i

    return -1


petrolpumps = [[1, 5], [10, 3], [3, 4]]
print(truckTour(petrolpumps))
