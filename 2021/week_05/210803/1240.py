import sys
import copy
from collections import deque
sys.setrecursionlimit(10 ** 6)
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
stack = []

def dfs(start, end):
    queue = deque()
    queue.append(start)
    visit = [-1] * (n + 1)
    visit[start] = 0
    while queue:
        cur = queue.popleft()
        if cur == end: 
            break
        for adj_node, adj_dist in graph[cur]:
            if visit[adj_node] > -1: continue
            visit[adj_node] = visit[cur] + adj_dist
            queue.append(adj_node)
    return visit[end]
                
for _ in range(n - 1):
    a, b, len = map(int, sys.stdin.readline().split())
    graph[a].append((b, len))
    graph[b].append((a, len))

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(dfs(a, b))
