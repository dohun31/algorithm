if __name__ == "__main__":
    n = int(input())

    dp = [[0 for _ in range(10)] for _ in range(n + 1)]
    dp[1] = [1] * 10
    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][0]
        for j in range(1, 10):
            dp[i][j] = sum(dp[i -1][:j + 1])
    print(sum(dp[-1]) % 10007)