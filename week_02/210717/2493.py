import sys

N = int(sys.stdin.readline().rstrip())
towers = list(map(int, sys.stdin.readline().split()))
result = []
indexs = []

for i in range(N):
    while indexs:
        if indexs[-1][1] > towers[i]:  # 수신 가능한 상황
            result.append(indexs[-1][0] + 1)
            break
        else:
            indexs.pop()
    if not indexs:  # 스택이 비면 레이저를 수신할 탑이 없다.
        result.append(0)
    indexs.append([i, towers[i]])  # 인덱스, 값

print(*result)