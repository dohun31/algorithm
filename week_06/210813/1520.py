import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

row, col = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]
dp = [[-1 for _ in range(col)] for _ in range(row)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

def dfs(x, y):
    if x == row - 1 and y == col - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for dx, dy in directions:
        nx = dx + x
        ny = dy + y
        if 0 <= nx < row and 0 <= ny < col and graph[nx][ny] < graph[x][y]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]

print(dfs(0, 0))