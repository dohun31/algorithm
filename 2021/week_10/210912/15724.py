import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # row, col
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = graph[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

k = int(input())
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    jjs =  dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(jjs) 