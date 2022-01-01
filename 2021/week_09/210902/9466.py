def dfs(idx):
    stack.append(idx)
    visited[idx] = True # 일단 방문함

    next_idx = graph[idx] # 현재 정점이 가리키는 정점
    if visited[next_idx]:
        if next_idx in stack:
            global cnt 
            cnt += len(stack[stack.index(next_idx):])
        return
    else:
        dfs(next_idx)


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**9)

    t = int(input()) # 테스트 케이스 개수

    for _ in range(t):
        n = int(input())
        graph = list(map(lambda x: int(x) - 1, input().split()))

        visited = [False for _ in range(n)] # 방문 여부
        cnt = 0 # 사이클에 포함되는 정점 개수를 세어줄 변수
        for idx, num in enumerate(graph):
            if not visited[idx]:
                stack = []
                dfs(idx)
        print(n - cnt)