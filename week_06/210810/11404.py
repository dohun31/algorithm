INF = int(1e9)
import sys
input = sys.stdin.readline
n, m = int(input()), int(input()) # n: 도시 수 , m: 버스 개수
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)] # 모든 간선 무한대로 초기화

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if not i == j:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end = ' ')
        else:
            print(graph[i][j], end = ' ')
    print()