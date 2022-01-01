if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    # 문자열 a, b 입력 받음
    a, b = input().rstrip(), input().rstrip()
    la, lb = len(a), len(b)
    # dp 테이블 초기화 행: lb + 1, 열: la + 1
    dp = [[0 for _ in range(la + 1)] for _ in range(lb + 1)]
    
    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            if a[i - 1] == b[j - 1]:
                dp[j][i] = dp[j - 1][i - 1] + 1
            else: dp[j][i] = max(dp[j][i - 1], dp[j - 1][i])

    print(dp[-1][-1])