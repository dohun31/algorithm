if __name__ == "__main__":
    n = int(input())
    s = input()
    dp = [[0, 0] for _ in range(n)]
    
    cnt = 0
    for i in range(n - 1, -1, -1):
        if s[i] == 'E':
            dp[i][1] = 1
        elif s[i] == 'H' and i < n - 1:
            dp[i][0] = (2 ** dp[i + 1][1]) - (1 + dp[i + 1][1])
        elif s[i] == 'W' and i < n - 1:
            cnt += dp[i + 1][0]
        if i < n - 1:
            dp[i][0] += dp[i + 1][0]
            dp[i][1] += dp[i + 1][1]
    print(cnt % 1000000007)