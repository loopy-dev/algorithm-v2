"""
h, w = 1, 1
h, w = 1, 2
h, w = 1, 3
h, w = 1, 4

블록은 수평하게만 놓을 수 있으며 n, m을 모두 채워야 한다.
같은 블록 형태가 나란히 올 수 없다.
빈 공간이 있으면 안된다.
"""
"""
1. 우선 한 줄의 [i]를 만드는데 필요한 경우의 수 구하기
2. 모든 층을 쌓았을 때 총 경우의 수 구하기
3. 불가능한 경우의 수 빼기

나쁜 레이아웃 제거 방법?
ex) 가로 길이가 4칸이라고 할 때, 최초로 잘리는 지점은 1, 2, 3이 된다.
나쁜 레이아웃의 경우, 잘리는 지점 왼쪽은 반드시 좋은 레이아웃이어야 하며, 오른쪽은 무엇이 들어오더라도 상관 없다.
answer[i]를 i번째 칸에서 좋은 레이아웃의 개수라고 할 때,
answer[i] = dp[i] - answer[i - 3] * block[i - 1] - answer[i - 2] * block[i - 2] - block[i - 1] * block[i - 3] - ...
"""
"""
dp 문제 회고 꼭하기!
"""

MOD = 10**9 + 7


def getOneRowPermutations(m):
    """
    calculate 1 floor permutations
    """
    dp = [0] * (m + 10)
    dp[0] = 1

    # calculate 1 floor permutations
    for i in range(1, m + 1):
        for j in range(1, 5):
            dp[i] += dp[i - j]
            dp[i] %= MOD

    return dp


def getAllRowPermutations(n, m):
    """
    calculate all floor permutations
    """
    dp = getOneRowPermutations(m)

    for i in range(len(dp)):
        dp[i] **= n
        dp[i] %= MOD

    return dp


def legoBlocks(n, m):
    dp = getAllRowPermutations(n, m)
    answer = [0] * (m + 10)

    # remove unstable cases
    for i in range(1, m + 1):
        answer[i] = dp[i]
        for j in range(i):
            answer[i] -= answer[j] * dp[i - j]
        answer[i] %= MOD

    return answer[m]


n = 1000
m = 1000
print(legoBlocks(n, m))
