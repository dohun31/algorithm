def solutio(n):
    dp = [1, 2]
    if n > 2:
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
    return dp[n - 1] % 1000000007

def solution(n):
    n1, n2 = 1, 2
    if n > 2:
        for _ in range(2, n):
            n1, n2 = n2, n1 + n2
    return n2 % 1000000007

print(solution(4))