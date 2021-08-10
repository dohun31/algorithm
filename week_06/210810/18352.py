import sys, heapq; input = sys.stdin.readline; INF = int(1e9)
n, m, k, x = map(int, input().split())
graph, distance = [[] for _ in range(n + 1)], [INF for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijkstra():
    q = []
    heapq.heappush(q, (0, x))
    distance[x] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra()
if k in distance:
    for idx, dist in enumerate(distance):
        if dist == k:
            print(idx)
else:
    print(-1)