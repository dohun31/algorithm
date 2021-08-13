dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def deal_water_cnt():
    for idx in list(water_cnt.keys()):
        x, y = map(int, idx.split())
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and graph[nx][ny] == 0:
                cnt += 1
        water_cnt[str(x) + " " + str(y)] = graph[x][y] - cnt if graph[x][y] - cnt > 0 else 0
        _graph[x][y] = water_cnt[str(x) + " " + str(y)]
        if _graph[x][y] == 0:
            del water_cnt[str(x) + " " + str(y)]

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < row and 0 <= ny < col and _graph[nx][ny] != 0 and not visited[nx][ny]:
            dfs(nx, ny)

if __name__ == "__main__":
    import sys, copy; sys.setrecursionlimit(10**6); input = sys.stdin.readline # 전처리
    row, col = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(row)]
    water_cnt = {str(i) + " " + str(j): 0 for i in range(1, row - 1) for j in range(1, col - 1) if graph[i][j] != 0}
    count = time_cnt = 0

    while True:
        if count == 2:
            print(time_cnt)
            quit()
        if not water_cnt:
            print(0)
            quit()
        count = 0; visited = [[False for _ in range(col)] for _ in range(row)] ; _graph = copy.deepcopy(graph)
        deal_water_cnt()
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if _graph[i][j] != 0 and not visited[i][j]:
                    dfs(i, j)
                    count += 1
        time_cnt += 1
        graph = copy.deepcopy(_graph)