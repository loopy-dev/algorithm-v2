"""
Max Min

max(arr') - min(arr')

unfairness 값이 최소가 되도록해야 한다.

주의해야 할 점은 n의 크기가 10**5인데 k도 10**5일 수 있다는 점이다.
"""
"""
1. 정렬을 우선 진행한다. 인접한 숫자일 수록 min max의 차이가 작아질 확률이 높기 때문이다.
2. 모든 배열의 길이를 구할 필요는 없다. 정렬 후에 첫 번째 인덱스와 마지막 인덱스를 구하면 된다.
"""
INF = 987654321


def maxMin(k, arr):
    arr.sort()
    answer = INF

    for i in range(k - 1, len(arr)):
        min_value = arr[i - k + 1]
        max_value = arr[i]

        answer = min(answer, max_value - min_value)

    return answer


# arr = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
# k = 4
arr = [1, 4, 7, 2]
k = 2
print(maxMin(k, arr))
