import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

data = [False] * (N + 1) 
heap = []

print(data)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    data[a] = True
    heapq.heappush(heap, (b, -1 * a))

for i in range(1, N + 1):
    if data[i] == False:
        heapq.heappush(heap, (i, -1 * i))
        data[i] = True

result = []
for _ in range(N):
    result.append(-1 * heapq.heappop(heap)[1])

print(" ".join(map(str, result)))
