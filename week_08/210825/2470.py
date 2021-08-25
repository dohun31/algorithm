import sys, heapq
input = sys.stdin.readline

n = int(input())
q = []
for num in map(int, input().split()):
    heapq.heappush(q, (abs(num), num))

result = [0, 0]
n1 = heapq.heappop(q)
min_sum = int(1e9)
while q:
    n2 = heapq.heappop(q)
    if abs(n1[1] + n2[1]) < min_sum:
        min_sum = abs(n1[1] + n2[1])
        result[0] = min(n1[1], n2[1])
        result[1] = max(n1[1], n2[1])
    n1 = n2

print(*result)