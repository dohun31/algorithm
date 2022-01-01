import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
numbers = [False] * (max(map(max, graph)) + 1)
for gs in graph: 
    for g in gs:
        if not numbers[g]:
            numbers[g] = True
indexs = [i for i in range(len(numbers)) if numbers[i]]

def new_graph():
    _graph = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            _graph[i][j] = graph[i][j]
    return _graph

def dfs(x, y, idx):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    global _graph
    _graph[x][y] = idx
    for cx, cy in zip(dx, dy):
        nx = cx + x
        ny = cy + y
        if 0 <= nx < N and 0 <= ny < N and _graph[nx][ny] > idx:
            dfs(nx, ny, idx)

max_count = 1
for idx in indexs:
    _graph = new_graph()
    count = 0
    for i in range(N):
        for j in range(N):
            if _graph[i][j] > idx:
                dfs(i, j, idx)
                count += 1
    max_count = max(count, max_count)

print(max_count)