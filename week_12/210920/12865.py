if __name__ == "__main__":
    n, k = map(int, input().split())
    datas = sorted(list(filter(lambda x: x[0] <= k,[list(map(int, input().split())) for _ in range(n)])))
    end = 0
    w_sum, v_sum = datas[end][0], datas[end][1] 
    result = 0
    l = len(datas)
    for start in range(l):
        while end < l - 1 and w_sum + datas[end + 1][0] <= k:
            end += 1
            w_sum += datas[end][0]
            v_sum += datas[end][1]
        if w_sum <= k:
            result = max(result, v_sum)
        w_sum -= datas[start][0]
        v_sum -= datas[start][1]
        print(result)
    print(result)