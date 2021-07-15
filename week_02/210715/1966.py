from collections import deque
import sys

N = int(input())

for _ in range(N):
    n, target = map(int, sys.stdin.readline().split())
    datas = list(map(int, sys.stdin.readline().split()))
    queue = []
    result = 1

    for i, data in enumerate(datas):
        queue.append([data, i])
    queue = deque(queue)
    datas.sort()

    while queue:
        data = queue.popleft()
        if data[1] == target:
            if data[0] == datas[-1]:
                print(result)
                break
            else:
                queue.append(data)
        else:
            if data[0] == datas[-1]:
                result += 1
                datas.pop()
            else:
                queue.append(data)
                