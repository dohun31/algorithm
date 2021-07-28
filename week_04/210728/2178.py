from collections import deque
import sys
sys.setrecursionlimit(10**6)
height, width = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(height)]
queue = deque()
visited = [[False] * width for _ in range(height)]

queue.append((0, 0))
visited[0][0] = True

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while queue:
    x, y = queue.popleft()
    for cx, cy in zip(dx, dy):
        nx = cx + x
        ny = cy + y
        if 0 <= nx < height and 0 <= ny < width:
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = True

print(graph[height - 1][width - 1])
