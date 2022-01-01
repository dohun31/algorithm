if __name__ == "__main__":
    n = int(input())
    dp = [[0] * n for _ in range(n)]
    dp[0] = [0, 1]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1] # sum(dp[i - 1])
        dp[i][1] = dp[i - 1][0]
    print(sum(dp[-1]))