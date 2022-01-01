def solution(n, s, a, b, fares):
    INF = int(1e9)
    d = [[INF for _ in range(n)] for _ in range(n)]
    # 인접 행렬
    for f in fares:
        x, y, dist = f
        x, y = x - 1, y - 1
        d[x][y] = dist
        d[y][x] = dist
    # 플로이드 와샬
    for k in range(n):
        d[k][k] = 0
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    # 최단 거리 찾기
    min_dist = INF
    for k in range(n):
        min_dist = min(min_dist, d[s - 1][k] + d[k][a - 1] + d[k][b - 1])
    return min_dist

n = 7
s = 3
a = 4
b = 1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
print(solution(n, s, a, b, fares))