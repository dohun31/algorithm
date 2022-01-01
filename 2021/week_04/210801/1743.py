def dfs(x, y):
    global count
    df = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
    visited[x][y] = True
    for d in df:
        nx = d[0] + x
        ny = d[1] + y
        if 0 <= nx <  row and 0 <= ny < col and graph[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)
            count += 1


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(10**6)
    # 초기 세팅
    row, col, k = map(int, sys.stdin.readline().split())
    dots = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
    graph = [[0 for _ in range(col)] for _ in range(row)]
    visited = [[False for _ in range(col)] for _ in range(row)]
    for dot in dots:
        graph[dot[0] - 1][dot[1] - 1] = 1
    # 덩어리 찾기 시작
    max_count = 0
    count = 0
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1 and not visited[i][j]:
                count += 1
                dfs(i, j)
                max_count = max(max_count, count)
                count = 0
    print(max_count)