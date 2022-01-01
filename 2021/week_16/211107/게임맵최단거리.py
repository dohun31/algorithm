def solution(maps):
    from collections import deque
    row, col = len(maps), len(maps[0])
    visited = [[0 for _ in range(col)] for _ in range(row)]

    q = deque()
    q.append((0, 0))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우

    while q:
        ni, nj = q.popleft()
        visited[ni][nj] = 1
        for di, dj in directions:
            ci = ni + di
            cj = nj + dj
            if 0 <= ci < row and 0 <= cj < col:
                if maps[ci][cj] == 1 and not visited[ci][cj]:
                    maps[ci][cj] = maps[ni][nj] + 1
                    q.append((ci, cj))
    result = maps[row - 1][col - 1]

    return result if result > 1 else -1

if __name__ == "__main__":
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    print(solution(maps))