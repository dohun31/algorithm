def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    graph = [[INF for _ in range(N)] for _ in range(N)]

    for i, j, dist in road:
        # 도로가 여러개일 가능성
        graph[i - 1][j - 1] = min(graph[i - 1][j - 1], dist)
        graph[j - 1][i - 1] = min(graph[j - 1][i - 1], dist)

    for i in range(N):
        graph[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for dist in graph[0]:
        if dist <= K:
            answer += 1

    return answer

if __name__ == "__main__":
    N = 6
    road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
    K = 4
    print(solution(N, road, K))