def solution(board):
    row, col = len(board), len(board[0])
    dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + board[i - 1][j - 1]
    
    for k in range(min(row, col), -1, -1):
        for i in range(k, row + 1):
            for j in range(k, col + 1):
                nowv = dp[i][j] - dp[i - k][j] - dp[i][j - k] + dp[i - k][j - k]
                if nowv == k ** 2:
                    return nowv

if __name__ == "__main__":
    board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
    print(solution(board))