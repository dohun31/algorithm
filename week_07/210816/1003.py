import sys
input = sys.stdin.readline

def fibonacci(n):
    dp = [[1, 0], [0, 1]] # dp 기본 세팅
    if n > 1: # n이 2이상이면 bottom-up
        for i in range(2, n + 1):
            dp.append([dp[i - 2][0] + dp[i - 1][0], dp[i - 2][1] + dp[i - 1][1]]) # 행렬 덧셈 (dp[i - 2] + dp[ i - 1])
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    print(*fibonacci(n))