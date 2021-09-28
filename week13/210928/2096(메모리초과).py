# 메모리 초과
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    datas = [list(map(int, input().rstrip().split())) for _ in range(n)]

    dp = [[[0, 0] for _ in range(n)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0][0] = min(dp[i - 1][0][0], dp[i - 1][1][0]) + datas[i - 1][0]
        dp[i][n - 1][0] = min(dp[i - 1][n - 1][0], dp[i - 1][n - 2][0]) + datas[i - 1][n - 1]
        dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][1][1]) + datas[i - 1][0]
        dp[i][n - 1][1] = max(dp[i - 1][n - 1][1], dp[i - 1][n - 2][1]) + datas[i - 1][n - 1]
        for j in range(1, n - 1):
            dp[i][j][0] = min(dp[i - 1][j - 1][0], dp[i - 1][j][0], dp[i - 1][j + 1][0]) + datas[i - 1][j]
            dp[i][j][1] = max(dp[i - 1][j - 1][1], dp[i - 1][j][1], dp[i - 1][j + 1][1]) + datas[i - 1][j]

    result = [int(1e9), -1]
    for d in dp[-1]:
        result[0] = min(result[0], d[0])
        result[1] = max(result[1], d[1])
    
    print(*result[::-1])