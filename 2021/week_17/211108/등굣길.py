def solution(m, n, puddles):
    dp = [[1 for _ in range(m)] for _ in range(n)]
    for j, i in puddles:
        dp[i - 1][j - 1] = 0
    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            if dp[i][j] == 1:
                dp[i][j] = (dp[i + 1][j] + dp[i][j + 1]) % 1000000007
    return dp[0][0]

if __name__ == "__main__":
    m = 4
    n = 3
    puddles = [[1,3],[3,1]]
    print(solution(m, n, puddles))