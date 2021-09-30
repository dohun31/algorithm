if __name__ == "__main__":
    n, m = map(int, input().split())
    datas = list(map(int, input().split()))

    result = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                now_sum = datas[i] + datas[j] + datas[k]
                if now_sum <= m:
                    result = max(result, now_sum)
    print(result)