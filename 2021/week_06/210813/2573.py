import sys; sys.setrecursionlimit(10**6); input = sys.stdin.readline
from collections import deque

def bfs(i, j, visited):
    queue = deque([[i, j]])
    melting_queue = deque([])
    visited[i][j] = True
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        cx, cy = queue.popleft()
        melt_cnt = 0
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                if graph[nx][ny] != 0:
                    visited[nx][ny]
                    queue.append([nx, ny])
                else:
                    melt_cnt += 1
        if melt_cnt:
            melting_queue.append((cx, cy, melt_cnt))
    
    return melting_queue

if __name__ == "__main__":
    row, col = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(row)]
    year = 0

    while True:
        count = 0
        visited = [[False for _ in range(col)] for _ in range(row)]
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if graph[i][j] != 0 and not visited[i][j]:
                    melting = bfs(i, j, visited)
                    count += 1
                    while melting:
                        x, y, c = melting.popleft()
                        graph[x][y] = max(graph[x][y] - c, 0)

        if count == 0:
            year = 0
            break
        if count >= 2:
            print(year)
            break
        year += 1