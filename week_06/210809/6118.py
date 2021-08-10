import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [[]]
visited = [False for _ in range(n + 1)]
queue = deque()

def bfs():
    while queue:
        nx, nl = queue.popleft() # 노드와 거리
        visited[nx] = True
        for i in graph[nx]: # 지금 노드를 또 큐에 넣어줌
            if not visited[i]: # 들리지 않은 노드만 넣어줌
                queue.append((i, nl + 1))
        if nl >= len(distance): # 1번과의 거리가 nl인 노드가 처음이라면
            distance.append([]) # 할당
        distance[nl].append(nx) # 거리 체크


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = True
for i in graph[1]:
    queue.append((i, 1))
distance[0].append(1)
bfs()

print(sorted(distance[-1])[0], len(distance) - 1, len(distance[-1]))