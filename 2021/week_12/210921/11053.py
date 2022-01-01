if __name__ == "__main__":
    n = int(input())
    datas = [0] + list(map(int, input().split()))

    l = len(datas)
    dp = [0] * (l)
    for i in range(1, l):
        for j in range(0, i):
            if datas[i] > datas[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    print(max(dp))