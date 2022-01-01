import sys
sys.setrecursionlimit(10 ** 6)
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

def dfs(x, y, count):
    global result
    result += 1
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    graph[x][y] = count
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
            dfs(nx, ny, count)
    

count = -1
result = 0
result_count = []
for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            dfs(x, y, count)
            result_count.append(result)
            result = 0
            count -= 1

print(len(result_count))
for cnt in sorted(result_count):
    print(cnt)