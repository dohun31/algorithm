if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    row, col = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(row)]

    result = 64
    for i in range(row - 7):
        for j in range(col - 7):
            change_cnt = 0
            idx = 0
            for x in range(i, i + 8):
                for y in range(j, j + 8):
                    if idx % 2 == 0:
                        if graph[x][y] != 'W':
                            change_cnt += 1
                    else:
                        if graph[x][y] != 'B':
                            change_cnt += 1
                    if y != j + 7:
                        idx += 1
            result = min(result, min(change_cnt, 64 - change_cnt))
    print(result)