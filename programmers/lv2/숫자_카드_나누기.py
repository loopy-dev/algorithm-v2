def solution(arrayA, arrayB):
    answer = 0
    arrayA.sort()
    arrayB.sort()

    answer = max(solve(arrayA, arrayB), solve(arrayB, arrayA))
    return answer


def get_gcd(a, b):
    if a < b:
        a, b = b, a

    if b == 0:
        return a

    return get_gcd(b, a % b)


def solve(arr_a, arr_b):
    gcd = arr_a[0]
    for i in range(1, len(arr_a)):
        gcd = get_gcd(gcd, arr_a[i])

    if gcd == 1:
        return 0

    for i in range(len(arr_b)):
        if arr_b[i] % gcd == 0:
            return 0

    return gcd


arrayA = [14, 35, 119]
arrayB = [18, 30, 102]
print(solution(arrayA, arrayB))
