if __name__ == "__main__":
    import sys
    input, print = sys.stdin.readline, sys.stdout.write

    n = int(input())
    datas = list(map(int, input().rstrip().split()))
    l = len(datas)

    dp = datas[:]
    result = 0
    for i in range(l):
        now_d = dp[i]
        for j in range(i, -1, -1):
            if datas[i] > datas[j]:
                dp[i] = max(dp[i], now_d + dp[j])
        result = max(result, dp[i])
    
    print(str(result))