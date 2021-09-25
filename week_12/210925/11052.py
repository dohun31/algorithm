if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    datas = list(map(int, input().rstrip().split()))

    dp = datas
    for i in range(n):
        for j in range((i + 1) // 2):
            dp[i] = max(dp[i], dp[j] + dp[i - j - 1])
    print(dp[-1])