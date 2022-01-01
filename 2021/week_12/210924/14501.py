if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    print = sys.stdout.write

    n = int(input())
    datas = [list(map(int, input().rstrip().split())) for _ in range(n)]

    dp = [0] * (n + 1) # 1차원으로 풀 때
    # result = 0
    # dp = [[0, 0] for _ in range(n + 1)] # 2차원으 풀 때
    for i in range(n - 1, -1, -1):
        t, p = datas[i]
        dp[i] = dp[i + 1] if i + t > n else max(dp[i + 1], dp[i + t] + p)
        # if i + t <= n:
        #     dp[i][1] = max(dp[i + t]) + p
        # dp[i][0] = max(dp[i + 1])
        # result = max(result, max(dp[i]))

    print(str(max(dp)))