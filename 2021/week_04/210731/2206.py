import sys
from collections import deque

def bfs():
    q.append([0, 0, 0])
    vis[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        for i in range(4):
            dx = x + dir[i][0]
            dy = y + dir[i][1]
            if 0 <= dx < n and 0 <= dy < m:
                # 아직 방문하지 않았고, 갈 수 있는 경우
                # 벽을 뚫고온 배열이면 벽을 뚫고온 배열에, 아니면 뚫고 오지 않은 배열에 1을더한다.
                if arr[dx][dy] == 0 and vis[dx][dy][z] == -1:
                    vis[dx][dy][z] = vis[x][y][z] + 1
                    q.append([dx, dy, z])
                # 벽을 뚫고오지 않은 배열이고 갈려는 곳에 벽이 있을 때
                elif z == 0 and arr[dx][dy] == 1 and vis[dx][dy][1] == -1:
                    vis[dx][dy][1] = vis[x][y][z] + 1
                    q.append([dx, dy, 1])
                    
n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip())))

# 방문을 하지 않았다는 표시는 -1로 하고 여기에 최단 경로의 수가 저장이 됩니다.
vis = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
# bfs로 돌 큐 선언
q = deque()
# 방향 탐색을 위한 dir 배열
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

bfs()

# ans1은 벽을 한번도 뚫지 않고 왔을 때의 최단경로,
# ans2는 벽을 한번 뚫고 왔을 때의 최단경로가 저장됩니다.
ans1, ans2 = vis[n - 1][m - 1][0], vis[n - 1][m - 1][1]

if ans1 == -1 and ans2 != -1:
    print(ans2)
elif ans1 != -1 and ans2 == -1:
    print(ans1)
else:
    print(min(ans1, ans2))