if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    row, col = map(int, input().split())
    datas = [list(input().rstrip()) for _ in range(row)]
    
    result = 0
    for k in range(min(row, col) - 1, -1, -1):
        for i in range(k, row):
            for j in range(k, col):
                if datas[i][j] == datas[i - k][j] == datas[i][j - k] == datas[i - k][j - k]:
                    result = max(result, (k + 1) ** 2)
                    print(result)
                    quit()