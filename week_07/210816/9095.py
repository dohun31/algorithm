import sys
input = sys.stdin.readline

def solution(n): # bottom-up 
    dp = [0] * (n + 1)
    dp[:4] = [0, 1, 2, 4]
    if n > 3:
        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] # i-1번쨰에서 '+1', i-2번째에서 '+2', i-3번째에서 '+3'
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    print(solution(n))