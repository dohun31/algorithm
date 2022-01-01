def solution(board, skill):
    row, col = len(board), len(board[0])
    dp = [[0 for _ in range(col + 2)] for _ in range(row + 2)]
    def apply_skill(r1, c1, r2, c2, d):
        dp[r1][c1] -= d
        dp[r2 + 1][c1] += d
        dp[r1][c2 + 1] += d
        dp[r2 + 1][c2 + 1] -= d
    
    for type, r1, c1, r2, c2, degree in skill:
        if type == 2: degree = -degree
        apply_skill(r1 + 1, c1 + 1, r2 + 1, c2 + 1, degree)
    
    cnt = 0
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            dp[i][j] += dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
            if board[i - 1][j - 1] + dp[i][j] > 0: cnt += 1
    
    return cnt

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))

# [1, 0, 0, 0, 1]
# [3, 2, 0, 0, 1]
# [1, 0, -2, -2, 1]
# [3, 2, 0, 0, 1]