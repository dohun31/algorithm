import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
towers = list(map(int, sys.stdin.readline().split()))
result = [0] * N
indexs = deque([])

# 뒤에서부터 탐색
for i in range(N - 1, -1, -1):
    # 해결하지 못한 index에 접근
    for _ in range(len(indexs)):
        index = indexs.popleft()
        # 수신 가능하면
        if towers[index] < towers[i]:
            result[index] = i + 1 
        else:
            indexs.append(index)
    indexs.append(i)

print(*result)