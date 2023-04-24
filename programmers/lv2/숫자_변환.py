# dp로 해결
# arr[x] = 0
# 만약 i % 3 == 0 이고 i // 3 >= x라면 min(arr[i], arr[i // 3] + 1)

INF = 987654321


def solution(x, y, n):
    arr = [INF] * 1000001
    arr[x] = 0

    for i in range(x + 1, y + 1):
        if i % 2 == 0 and i // 2 >= x:
            arr[i] = min(arr[i], arr[i // 2] + 1)

        if i % 3 == 0 and i // 3 >= x:
            arr[i] = min(arr[i], arr[i // 3] + 1)

        if i - n >= x:
            arr[i] = min(arr[i], arr[i - n] + 1)

    return arr[y] if arr[y] < INF else -1


x = 2
y = 5
n = 4
print(solution(x, y, n))
