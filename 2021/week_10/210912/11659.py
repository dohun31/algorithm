import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(n):
    dp[i + 1] = dp[i] + graph[i]

for _ in range(m):
    a, b = map(int, input().split())
    result = dp[b] - dp[a - 1]
    print(result)