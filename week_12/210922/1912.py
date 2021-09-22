if __name__ == "__main__":
    n = int(input())
    datas = list(map(int, input().split()))

    l = len(datas)
    dp = [0] * (l + 1)
    for i in range(1, l + 1):
        dp[i] = max(dp[i - 1] + datas[i - 1], datas[i - 1]) # 앞에꺼랑 더하거나, 안 더하거나
    
    print(max(dp[1:]))