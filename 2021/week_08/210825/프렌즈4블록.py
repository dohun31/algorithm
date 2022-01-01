def solution(m, n, board):
    stack = []
    directions = [(1, 0), (0, 1), (1, 1)]
    board = list(map(list, board))
    result = 0
    while True:
        for i in range(m):
            for j in range(n):
                flag = True
                cnt = 0
                for dx, dy in directions:
                    if 0 <= i + dx < m and 0 <= j + dy < n and board[i][j] != 0:
                        if board[i][j] != board[i + dx][j + dy]:
                            flag = False
                        else:
                            cnt += 1
                flag and cnt == 3 and stack.append((i, j))
    
        if not stack:
            break
        else:
            while stack:
                i, j = stack.pop()
                if board[i][j] != 0:
                    result += 1
                board[i][j] = 0
                for dx, dy in directions:
                    if board[i + dx][j + dy] != 0:
                        result += 1
                    board[i + dx][j + dy] = 0
        
        for _ in range(10):
            for j in range(n):
                for i in range(m - 1):
                    if board[i][j] != 0 and board[i + 1][j] == 0:
                        board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

    return result

m = 4
n = 4
board = ["ABCD", "BACE", "BCDD", "BCDD"]
for p in board:
    print(p)
print(solution(m, n, board))