if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    datas = list(map(int, input().rstrip().split()))
    
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if datas[j] > datas[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
