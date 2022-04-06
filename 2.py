def dfs(i, target, visited, answer):
    visited[i] = True
    if i == target:
        return True
    for next in graph[i]:
        if not visited[next]:
            answer.append(houses[next])
            if not dfs(next, target, visited, answer):
                answer.pop()
            else:
                return True
    return False

if __name__ == "__main__":
    n, q = map(int, input().split())
    houses = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    play = []

    for _ in range(n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for _ in range(q):
        a, b = map(lambda x: int(x) - 1, input().split())
        play.append((a, b))
    
    for x, y in play:
        answer = [houses[x]]
        visited = [False for _ in range(n)]
        dfs(x, y, visited, answer)
        print(int(''.join(map(str, answer))) % 1000000007)
