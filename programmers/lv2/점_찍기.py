# 점 찍기
import math

def solution(k, d):
    answer = 0

    for i in range(0, d + 1, k):
        y = int(math.sqrt(d ** 2 - i ** 2))
        answer += (y // k) + 1

    return answer

k = 1 
d = 5
print(solution(k ,d))