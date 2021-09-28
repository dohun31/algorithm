if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    up_datas = list(map(int, input().rstrip().split()))
    down_datas = up_datas[::-1]

    dp = [[1, 1] for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if up_datas[i] > up_datas[j]:
                dp[i][0] = max(dp[i][0], dp[j][0] + 1)
            if down_datas[i] > down_datas[j]:
                dp[i][1] = max(dp[i][1], dp[j][1] + 1)
                
    result = 0
    for i in range(n):
        result = max(result, dp[i][0] + dp[n - 1 - i][1] - 1)

    print(result)