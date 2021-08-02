import sys
sys.setrecursionlimit(10 ** 6)
N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
parent_node = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    for i in graph[start]:
        if parent_node[i] == 0:
            parent_node[i] = start
            dfs(i)

dfs(1)

for i in range(2, N + 1):
    print(parent_node[i])