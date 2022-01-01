def solution(W, H):
    import numpy as np
    import math
    # 직선 방정식 구하기
    graph = [[1for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            dist = round((i *  W - j * H) / math.sqrt(H ** 2 + W ** 2))
            #     graph[i][j] = -1
            if -1 < dist < 1:
                graph[i][j] = 0
    graph = np.array(graph)
    for i in range(H):
        for j in range(W):
            if graph[i][j] == 1 and np.array_equal(graph[i:i+2, j+1:j+2], [[0], [0]]):
                graph[i][j] = 0
    return np.count_nonzero(graph)

if __name__ == "__main__":
    W = 8
    H = 12
    print(solution(W, H))