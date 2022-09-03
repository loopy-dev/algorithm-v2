def transform(n):
    if n % 3 == 0:
        return "4"
    elif n % 3 == 1:
        return "1"
    return "2"


def solution(n):
    answer = ""
    while n > 0:
        answer = transform(n) + answer
        if n % 3 == 0:
            n //= 3
            n -= 1
        else:
            n //= 3
    return answer


for i in range(1, 11):
    print(solution(i))
