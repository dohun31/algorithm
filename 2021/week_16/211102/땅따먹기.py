def solution(land):
    row, col = len(land), len(land[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]
    dp[-1] = land[-1]
    for i in range(row - 2, -1, -1):
        for j in range(col):
            dp[i][j] = max(dp[i + 1][:j] + dp[i + 1][j + 1:]) + land[i][j]
    return max(dp[0])

if __name__ == "__main__":
    land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
    print(solution(land))