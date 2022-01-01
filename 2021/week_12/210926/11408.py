if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    # 입력
    row, col = map(int, input().split())
    datas = []
    for _ in range(row):
        datas.append(list(map(int, input().split())))
    # dp
    dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + datas[i - 1][j - 1]
    
    print(dp[-1][-1])