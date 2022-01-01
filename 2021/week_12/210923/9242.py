if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    a = input().rstrip()
    b = input().rstrip()

    la, lb = len(a), len(b)
    dp = [[0 for _ in range(la + 1)] for _ in range(lb + 1)]
    for i in range(1, lb + 1):
        for j in range(1, la + 1):
            if a[j - 1] == b[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    result_cnt = dp[-1][-1]
    print(result_cnt)

    result_str = ""
    row, col = lb, la
    while result_cnt > 0:
        if result_cnt - 1 == dp[row][col - 1] and result_cnt - 1 == dp[row - 1][col]:
            result_str = a[col - 1] + result_str
            result_cnt -= 1
            row -= 1
            col -= 1
        else:
            if dp[row - 1][col] > dp[row][col - 1]:
                row -= 1
            else:
                col -= 1
    print(result_str)