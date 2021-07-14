from collections import deque

N, K = map(int, input().split())
queue = deque()
result = []

for i in range(1, N + 1):
    queue.append(i)

i = 1
while queue :
    data = queue.popleft()
    if i == K:
        result.append(str(data))
        i = 1
    else:
        queue.append(str(data))
        i += 1

print('<' + ", ".join(result) + '>')