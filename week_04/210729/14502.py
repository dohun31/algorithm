from collections import deque
from itertools import combinations
import copy
import sys
sys.setrecursionlimit(10**6)

def bfs(x, y):
    queue.append((x, y))
    di = [-1, 0, 1, 0]
    dj = [0, -1, 0, 1]
    while queue:
        i, j = queue.popleft()
        for ci, cj in zip(di, dj):
            ni = ci + i
            nj = cj + j
            if 0 <= ni < n and 0 <= nj < m and _graph[ni][nj] == 0 and not _visited[ni][nj]:
                _visited[ni][nj] = True
                _graph[ni][nj] = 2
                queue.append((ni, nj))

if __name__=="__main__":
    n, m = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    zero = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]
    queue = deque()

    max_count = 0
    for points in combinations(zero, 3):
        _graph = copy.deepcopy(graph)
        _visited = copy.deepcopy(visited)
        for point in points:
            _graph[point[0]][point[1]] = 1
        # 바이러스 전염
        count = 0
        for i in range(n):
            for j in range(m):
                if _graph[i][j] == 2 and not _visited[i][j]:
                    bfs(i, j)
        # 안전 영역 개수 구하기
        for g in _graph:
            count += g.count(0)
        max_count = max(max_count, count)
    print(max_count)