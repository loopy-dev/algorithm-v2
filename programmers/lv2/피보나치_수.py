MOD = 1234567


def solution(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append((dp[i - 1] + dp[i - 2]) % MOD)
    return dp[n]


n = 5
print(solution(n))
