"""
Between two sets
1. 첫 번째 배열의 모든 요소로 어떤 정수를 나누었을 때 나누어 떨어진다.
2. 두 번째 배열의 모든 요소를 어떤 정수로 나누었을 때 나누어 떨어진다.
len(arr1), len(arr2) <= 10
"""
"""
1. 여러 수의 공배수라면 나누어 떨어질 수 있다.
2. 여러 수의 공약수라면 나누어 떨어질 수 있다.

따라서 어떤 수는 첫 번째 배열의 공배수이면서 두 번째 배열의 공약수여야 한다.

1. b 배열의 최대 공약수를 우선 구한다.
2. 해당 공약수의 약수들을 구한 다음, 그 숫자가 a 배열의 숫자로 나누어 떨어질 수 있는지 구한다.
3. 개수를 센다.
"""

def get_gcd(a, b):
    if a < b:
        a, b = b, a

    if b == 0:
        return a

    return get_gcd(b, a % b)


def get_gcd_list(arr):
    gcd = arr[0]
    for i in range(1, len(arr)):
        gcd = get_gcd(gcd, arr[i])

    gcd = get_gcd(gcd, arr[0])
    return gcd


def getTotalX(a, b):
    gcd_b = get_gcd_list(b)
    common_divisors = set()

    # get common divisor
    for i in range(1, int(gcd_b**0.5) + 1):
        if gcd_b % i == 0:
            common_divisors.add(i)
            common_divisors.add(gcd_b // i)

    count = 0

    for c in common_divisors:
        flag = True
        for factor in a:
            if c < factor:
                flag = False
                break

            if c % factor > 0:
                flag = False
                break

        if flag:
            count += 1

    return count
