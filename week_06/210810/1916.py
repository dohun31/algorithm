INF = int(1e9); import sys, heapq; input = sys.stdin.readline

n, m = int(input()), int(input()) # 도시, 버스 개수
graph = [[] for _ in range(n + 1)] # 인접 리스트
distance = [INF] * (n + 1) # 거리 기록

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra():
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra()
print(distance[end])