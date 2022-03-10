import sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    points = [list(map(lambda x: int(x) - 1, sys.stdin.readline().split())) for _ in range(m)]

    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n):
        for j in range(n):
            dp[i][j] += graph[i][j]
            if i == 0: dp[i][j] += dp[i][j - 1]
            elif j == 0: dp[i][j] += dp[i - 1][j]
            else: dp[i][j] += dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

    for x1, y1, x2, y2 in points:
        nowv = dp[x2][y2]
        if y1 > 0:
            nowv -= dp[x2][y1 - 1]
        if x1 > 0:
            nowv -= dp[x1 - 1][y2]
        if y1 > 0 and x1 > 0:
            nowv += dp[x1 - 1][y1 - 1]
        print(nowv)