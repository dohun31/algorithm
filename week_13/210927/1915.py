if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    row, col = map(int, input().split())
    datas = [list(map(int, list(input().rstrip()))) for _ in range(row)]

    dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            dp[i][j] += dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + datas[i - 1][j - 1]
    
    possible_l = min(row, col)
    max_area = 0
    for area in range(1, possible_l + 1):
        for i in range(area, row + 1):
            for j in range(area, col + 1):
                if max_area == area * area:
                    break
                now_area = dp[i][j] - dp[i][j - area] - dp[i-area][j] + dp[i - area][j - area]
                if now_area == area * area:
                    max_area = max(max_area, now_area)
                    break
    
    print(max_area)