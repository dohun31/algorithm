if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    datas = [list(map(int, input().split())) for i in range(n)]

    result = []
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i != j:
                if datas[i][0] < datas[j][0] and datas[i][1] < datas[j][1]:
                    cnt += 1
        result.append(cnt + 1)
    print(*result)