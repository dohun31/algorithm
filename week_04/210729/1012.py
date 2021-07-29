from collections import deque
import sys
sys.setrecursionlimit(10**6)

def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for cx, cy in zip(dx, dy):
            nx = cx + x
            ny = cy + y
            if 0 <= nx < row and 0 <= ny < col and graph[nx][ny] == 1 and not visited[nx][ny]:
                graph[nx][ny] = 0
                queue.append((nx, ny))

T = int(sys.stdin.readline())
for _ in range(T):
    # input + 초기 세팅
    col, row, num = map(int, sys.stdin.readline().split())
    graph  = [[0 for _ in range(col)] for _ in range(row)]
    visited = [[False for _ in range(col)] for _ in range(row)]
    for _ in range(num):
        c, r = map(int, sys.stdin.readline().split())
        graph[r][c] = 1
    # 탐색 시작
    queue = deque([])
    count = 0
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1 and not visited[i][j]:
                queue.append((i, j))
                bfs()
                # 한번의 탐색이 끝날때마다(한 덩어리마다) count를 세어 줌.
                count += 1
    print(count)