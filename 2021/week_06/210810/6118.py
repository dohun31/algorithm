import sys, heapq; input = sys.stdin.readline; INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dijkstra():
    q = []
    distance[1] = 0
    heapq.heappush(q, (0, 1))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra()

max_dist = max(distance[1:])
max_dist_idx = distance.index(max_dist)
max_dist_cnt = distance.count(max_dist)
print(max_dist_idx, max_dist, max_dist_cnt)