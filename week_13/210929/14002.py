if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    datas = list(map(int, input().split()))

    dp = [1] * n
    max_idx, max_value = 0, 0
    for i in range(n):
        for j in range(i):
            if datas[i] > datas[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        if max_value < dp[i]:
            max_idx, max_value = i, dp[i]
    
    result = [0] * max_value
    for i in range(max_idx, -1, -1):
        if dp[i] == max_value:
            result[max_value - 1] = datas[i]
            max_value -= 1
    
    print(len(result))
    print(*result)