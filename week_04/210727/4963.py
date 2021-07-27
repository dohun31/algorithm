import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    dx = [-1, 0, 1, 0, 1, 1, -1, -1]
    dy = [0, 1, 0, -1, 1, -1, 1, -1]
    graph[x][y] = 0
    for i in range(8):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < height and 0 <= ny < width and graph[nx][ny] == 1:
            dfs(nx, ny)
while True:
    width, height = map(int, sys.stdin.readline().split())
    if width == height == 0:
        break
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
    count = 0

    for i in range(height):
        for j in range(width):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)
