"""
Dynamic Array

2차원 빈 n개의 요소를 갖는 배열
arr = [[] for _ in range(n)]
lastAnswer = 0
queries:
1 x y: 
idx = (x ^ lastAnswer) % n
arr[idx].append(y)

2 x y:
idx = (x ^ lastAnswer) % n
lastAnswer = arr[idx][y % len(arr[idx])]
"""
"""
주어진 쿼리를 코드로 구현한다.
"""


def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    last_answer = 0
    answer = []

    # iterate queries and execute
    for q in queries:
        # type, number 1, number 2
        t, a, b = q

        idx = (a ^ last_answer) % n

        if t == 1:
            arr[idx].append(b)
        else:
            last_answer = arr[idx][b % len(arr[idx])]
            answer.append(last_answer)

    return answer
