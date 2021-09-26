if __name__ == "__main__":
    n, k = map(int, input().split())

    dp = [[0 for _ in range(n)] for _ in range(k)]
    dp[0] = [1] * n
    for i in range(1, k):
        dp[i][0] = dp[i - 1][0] + 1
        for j in range(1, n):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000
            
    print(dp[-1][-1])