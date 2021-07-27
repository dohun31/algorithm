import sys
sys.setrecursionlimit(10 ** 6)
m, n, k = map(int, sys.stdin.readline().split())
graph = [[1] * n for _ in range(m)]
for _ in range(k):
    points = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(points[1], points[3]):
        for j in range(points[0], points[2]):
            graph[i][j] = 0

def dfs(x, y):
    global point_count
    point_count  += 1
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    graph[x][y] = 0
    for cx, cy in zip(dx, dy):
        nx = cx + x
        ny = cy + y
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
            dfs(nx, ny)

point_count = 0
result = []
for x in range(m):
    for y in range(n):
        if graph[x][y] == 1:
            dfs(x, y)
            result.append(point_count)
            point_count = 0

print(len(result))
print(*sorted(result))