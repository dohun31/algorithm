N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

house_count = 1
danzi_count = []
count = 0

def dfs(x, y):
    global count
    global danzi_count
    if x < 0 or x > N - 1 or y < 0 or y > N - 1:
        return False

    if graph[x][y] == 1:
        count += 1
        graph[x][y] = -1 * house_count
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        if count != 0: danzi_count.append(count)
        count = 0
        return True
    return False

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            house_count += 1

print(house_count - 1)
for i in sorted(danzi_count):
    print(i)