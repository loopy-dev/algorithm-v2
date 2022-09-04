def solution(numbers):
    arr = list(map(lambda x: str(x), numbers))
    arr.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(arr)))


numbers = [3, 30, 34, 5, 9]
print(solution(numbers))
