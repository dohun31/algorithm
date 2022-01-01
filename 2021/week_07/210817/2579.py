import sys
input = sys.stdin.readline

n = int(input())
dp = []
stairs = []
for _ in range(n):
    stairs.append(int(input()))

if n >= 1:
    dp.append(stairs[0])
if n >= 2:
    dp.append(max(stairs[0] + stairs[1], stairs[1]))
if n >= 3:
    dp.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
    for i in range(3, n):
        dp.append(max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i]))

print(dp.pop())