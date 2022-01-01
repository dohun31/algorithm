def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        dp = [0 for _ in range(n)]
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
        return dp[-1]

if __name__ == "__main__":
    n = 1
    print(solution(n))