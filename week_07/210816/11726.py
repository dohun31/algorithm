import sys
input = sys.stdin.readline


def solution(n):
    dp[:3] = [0, 1, 2]
    if n > 2:
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

n = int(input())
dp = [0] * (n + 1)
print(solution(n) % 10007)