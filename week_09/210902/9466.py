def dfs(idx):
    if idx not in stack: # 현재 index stack에 넣기(중복 방지)
        stack.append(idx)
    next_idx = graph[idx] # 현재 정점이 가리키는 정점
    visited[idx] = True # 일단 방문함
    # 가리키는 정점이 target이랑 같다면
    if next_idx in stack:
        print(stack)
        global cnt
        cnt += len(stack[stack.index(next_idx):])
    else:
        if not visited[next_idx]: # 같지않고 방문하지 않은 정점이라면
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
                stack = [idx]
                dfs(idx)
        print(n - cnt)