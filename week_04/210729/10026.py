import sys
import copy
sys.setrecursionlimit(10**6)

def dfs(x, y, c):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    _visited[x][y] = True
    for cx, cy in zip(dx, dy):
        nx = cx + x
        ny = cy + y
        if 0 <= nx < n and 0 <= ny < n and _graph[nx][ny] == c and not _visited[nx][ny]:
            dfs(nx, ny, c)

if __name__=="__main__":
    n = int(sys.stdin.readline())
    graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
    n_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if n_graph[i][j] == 'G':
                n_graph[i][j] = 'R'

    graphs = [graph, n_graph]
    visited = [[False for _ in range(n)] for _ in range(n)]
    colors = [['R', 'G', 'B'], ['R', 'B']]

    for color, gp in zip(colors, graphs):
        count = 0
        _graph = copy.deepcopy(gp)
        _visited = copy.deepcopy(visited)
        for c in color:
            for i in range(n):
                for j in range(n):
                    if _graph[i][j] == c and not _visited[i][j]:
                        dfs(i, j, c)
                        count += 1

        print(count, end=' ')