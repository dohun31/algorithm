import heapq
import sys

N = int(input())

heap = []

for _ in range(N):
    data = int(sys.stdin.readline())
    if data == 0:
        if len(heap) > 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(data), data))
