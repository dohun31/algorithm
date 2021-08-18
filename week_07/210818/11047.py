import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0

for coin in coins[::-1]:
    necessary_coin = k // coin
    if necessary_coin > 0:
        cnt += necessary_coin
        k %= coin

print(cnt)