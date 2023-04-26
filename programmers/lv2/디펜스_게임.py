# 배열 정렬 -> 내림차순으로
# 인덱스를 구하고 이를 바탕으로 기존 배열의 인덱스 요소를 0으로 만들기
# 같은 개수에
import heapq


def solution(n, k, enemy):
    answer = 0
    count = k
    ally = n
    s = 0
    q = []
    for i in range(len(enemy)):
        s += enemy[i]
        heapq.heappush(q, -enemy[i])
        answer = i + 1

        while count > 0 and s > ally:
            count -= 1
            s -= -heapq.heappop(q)

        if s > ally:
            return answer - 1
    return answer


n = 2
k = 4
enemy = [3, 3, 3, 3]
print(solution(n, k, enemy))
