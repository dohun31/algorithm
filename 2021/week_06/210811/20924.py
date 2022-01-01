import sys; sys.setrecursionlimit(10**6); input = sys.stdin.readline

ans = {}

def find_giga(r):
    global len_gd
    if len(graph[r]) == 2:
        r, d = graph[r][0]
        len_gd += d
        return find_giga(r)
    else:
        return r

def dfs(x, d, sum):
    global len_gi
    sum = max(sum, sum + d)
    if len_gi < sum:
        len_gi = sum
    visited[x] = True
    for g in graph[x]:
        if not visited[g[0]]:
            dfs(g[0], g[1], sum)

if __name__ == "__main__":
    n, r = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [[False] for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, b))
    # 기둥 , 기가
    len_gd = 0
    giga = find_giga(r)
    # 가장 긴 가지 찾기
    len_gi = 0
    dfs(giga, 0, 0)
    
    print(len_gd, len_gi)