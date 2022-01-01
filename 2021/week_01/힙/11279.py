import heapq
import sys

N = int(input())

heap = []

for _ in range(N):
    data = int(sys.stdin.readline())
    if data == 0:
        if len(heap) > 0:
            print(-1 * heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -1 * data)