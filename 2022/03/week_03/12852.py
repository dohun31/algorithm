import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    dp = [[0, 0] for _ in range(n + 1)]

    dp[1] = [0, 1]
    for i in range(2, n + 1):
        min_value, min_idx = dp[i - 1][0], i - 1
        if i % 2 == 0 and min_value >= dp[i // 2][0]:
            min_value, min_idx = dp[i // 2][0], i // 2
        if i % 3 == 0 and min_value >= dp[i // 3][0]:
            min_value, min_idx = dp[i // 3][0], i // 3
        dp[i] = [min_value + 1, min_idx]
    
    print(dp[n][0])
    print(n, end=' ')
    while n > 1:
        print(dp[n][1], end =' ')
        n = dp[n][1]