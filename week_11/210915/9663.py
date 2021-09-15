def dfs(queens, n, row):
    count = 0
    # n개의 행에 퀸들이 있다면 종료 
    if n == row:
        return 1
    # 모든 열 탐색
    for col in range(n):
        queens[row] = col
        for x in range(row):
            # 같은 열에 있다면
            if queens[x] == queens[row]:
                break
            # 대각선에 있다면
            if abs(queens[x] - queens[row]) == (row - x):
                break
        else:
            count += dfs(queens, n, row + 1)
    
    return count

if __name__ == "__main__":
    n = int(input())
    print(dfs([0] * n,  n, 0))
