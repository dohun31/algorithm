import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
checked = [False for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1번은 나
checked[1] = True
count = 0
for nums in graph[1]: # 내 친구들 조사
    # 내 친구 체크
    if not checked[nums]:
        checked[nums] = True
        count +=1
    # 내 친구의 친구 체크
    for n in graph[nums]:
        if not checked[n]:
            checked[n] = True
            count += 1

print(count)