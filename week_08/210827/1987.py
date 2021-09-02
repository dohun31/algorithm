import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

row, col = map(int, input().split())
graph = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(row)]
check = [0] * 26

def dfs(x, y, cnt):
    global max_cnt
    max_cnt = max(cnt, max_cnt)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
    for dx, dy in directions:
        cx = x + dx
        cy = y + dy
        if 0 <= cx < row and 0 <= cy < col and not check[graph[cx][cy]]:
            check[graph[cx][cy]] = 1
            dfs(cx, cy, cnt + 1)
            check[graph[cx][cy]] = 0
            

check[graph[0][0]] = True
max_cnt = 0
dfs(0, 0, 1)

print(max_cnt)