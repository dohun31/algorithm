from collections import deque

N = int(input())
queue = deque()
result = []

for i in range(1, N + 1):
    queue.append(i)

while queue:
    result.append(queue.popleft())
    if queue:
        queue.append(queue.popleft())
        
print(*result)