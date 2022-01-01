import sys
from collections import deque
sys.setrecursionlimit(10**6)
col, row = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
visited = [[False for _ in range(col)] for _ in range(row)]

queue = deque([(i, j) for i in range(row) for j in range(col) if graph[i][j] == 1])

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def show_graph():
    for i in range(row):
        for j in range(col):
            print(graph[i][j], end=' ')
        print()

while queue:
    x, y = queue.popleft()
    last_x, last_y = x, y
    visited[x][y] = True
    for cx, cy in zip(dx, dy):
        nx = cx + x
        ny = cy + y
        if 0 <= nx < row and 0 <= ny < col and graph[nx][ny] == 0 and not visited[nx][ny]:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

flag = True
for i in range(row):
    for j in range(col):
        if graph[i][j] == 0:
            flag = False

print(graph[last_x][last_y] - 1) if flag else print(-1)