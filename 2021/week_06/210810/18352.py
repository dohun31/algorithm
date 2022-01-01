import sys, heapq; input = sys.stdin.readline; INF = int(1e9)
n, m, k, x = map(int, input().split())
graph, distance = [[] for _ in range(n + 1)], [INF for _ in range(n + 1)]
# 인접 리스트 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijkstra():
    q = []
    heapq.heappush(q, (0, x))
    distance[x] = 0
    while q:
        dist, now = heapq.heappop(q) # 거리, 현재 노드 번호
        if distance[now] < dist: # 현재 저장된 거리보다, 지금 거리가 더 크다면 무시
            continue
        for i in graph[now]: # 현재 노드와 연결된 노드들 비교
            cost = dist + 1 # 다음 노드까지의 비용은 현재 거리에서 1만큼 더한값과 같음
            if cost < distance[i]: # 현재 저장된 거리보다 cost가 작다면
                distance[i] = cost # 갱신하고
                heapq.heappush(q, (cost, i)) # 노드번호랑 거리 힙에 넣어줌

dijkstra()
if k in distance:
    for idx, dist in enumerate(distance):
        if dist == k:
            print(idx)
else:
    print(-1)