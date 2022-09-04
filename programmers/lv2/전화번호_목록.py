def solution(phone_book):
    numbers = list(map(lambda x: "".join(x.split(" ")), phone_book))
    numbers.sort()
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1][: len(numbers[i])]:
            return False
    return True


phone_book = ["117", "11937", "11938"]
print(solution(phone_book))
