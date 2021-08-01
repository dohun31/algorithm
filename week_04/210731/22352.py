import sys
sys.setrecursionlimit(10**6)
row, col = map(int, sys.stdin.readline().split())
nv_graph = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
v_graph = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
visited = [[False for _ in range(col)] for _ in range(row)]

def dfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visited[x][y] = True
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < row and 0 <= ny < col:
            if nv_graph[nx][ny] == nv_graph[x][y] and not visited[nx][ny]:
                if v_graph[nx][ny] != v_graph[x][y]:
                    print('NO')
                    quit()
                dfs(nx, ny)

count = 0
for i in range(row):
    for j in range(col):
        if count > 1:
            print('NO')
            quit()
        if nv_graph[i][j] != v_graph[i][j] and not visited[i][j]:
            dfs(i, j)
            count += 1

print('YES')