import sys
input = sys.stdin.readline

t = int(input())
dp = [0 for _ in range(101)]
dp[:3] = [0, 1, 1]

for i in range(3, 101):
    dp[i] = dp[i - 2] + dp[i - 3]

for _ in range(t):
    print(dp[int(input())])