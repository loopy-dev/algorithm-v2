"""
최소 몇번의 뇌물을 줘야만 주어진 큐를 만들 수 있는가?
ex) [1, 2, 3, 4, 5, 6, 7, 8] -> [1, 2, 3, 5, 4, 6, 7, 8]
한 번에 한 자리만 이동할 수 있다
"""
"""
직관적으로 접근하기
1. 직관적으로 접근한다면, [2, 1, 5, 4, 3]를 순회하면서, 앞과 뒤 숫자를 비교하고, 
다음 숫자가 현재 숫자보다 작다면 스왑 -> 무한 반복 -> 시간 초과 발생
2. 어차피 비교는 두 번째 뒷자리 까지만 비교하면 되기 때문에 큰 문제가 되지 않을 수도 있다.
[2, 1, 5, 4, 3]
[1, 2, 5, 4, 3]
[1, 2, 4, 5, 3]
[1, 2, 4, 3, 5]
[1, 2, 3, 4, 5]

"""
"""
더 최적화할 수 있는 방법?
O(N)으로 최적화할 수는 없을까?
"""

# 가장 정석적인 방법으로
def minimum_bribes(q):
    count = 0

    for i in range(len(q) - 1):

        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        for j in range(i, -1, -1):
            if q[j] > q[j + 1]:
                q[j], q[j + 1] = q[j + 1], q[j]
                count += 1

    print(count)


# 뒤에서 부터 한 칸과 두 칸만 탐색을 시도하면, 시간을 절약할 수 있다.
# 조금 우아하진 않은 방법이라고 생각하지만, 두 칸만 시도하면 되기 때문에
# 획기적으로 시간을 절약할 수 있는 방법이기는 하다.
def minimumBribes(q):
    count = 0
    for i in range(len(q) - 1, -1, -1):
        if q[i] == i + 1:
            continue

        if i - 1 >= 0 and q[i - 1] == i + 1:
            q[i - 1], q[i] = q[i], q[i - 1]
            count += 1

        elif i - 2 >= 0 and q[i - 2] == i + 1:
            q[i - 2], q[i - 1] = q[i - 1], q[i - 2]
            q[i - 1], q[i] = q[i], q[i - 1]
            count += 2

        else:
            print("Too chaotic")
            return

    print(count)


q = [1, 2, 5, 3, 7, 8, 6, 4]
# minimum_bribes(q)
minimumBribes(q)
