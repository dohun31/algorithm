import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

dp = [0] * (n + 2)
for _ in range(m):
    start, end, d = map(int, input().split())
    dp[start] += d
    dp[end + 1] -= d

for i in range(1, n + 1):
    dp[i] += dp[i - 1]
    num[i - 1] += dp[i]

print(*num)