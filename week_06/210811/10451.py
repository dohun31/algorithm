import sys; sys.setrecursionlimit(10**6); input = sys.stdin.readline

def dfs(n):
    visited[n] = 1 # 방문 처리
    if visited[graph[n]] == 0:
        dfs(graph[n])

t = int(input()) # test case

for _ in range(t):
    n = int(input()) # number of node
    graph = [0] * n
    visited = [0] * n

    for idx, num in enumerate(list(map(int, input().split()))):
        graph[idx] = num - 1 # index니까 -1 로 기록
    
    count = 0
    for n in graph:
        if visited[n] == 0: # 방문 하지 않은 노드라면 bfs하고 count++
            dfs(n)
            count += 1
    
    print(count)