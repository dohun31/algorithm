if __name__ == "__main__":
    n = int(input())
    datas = list(map(int, input().split()))
    datas = {data: 0 for data in datas}

    for data in datas.keys():
        now_data = data
        while True:
            if data % 3 == 0:
                datas[now_data] += 1
                data //= 3
            else:
                break
    
    result = sorted(datas.items(), key = lambda x:(-x[1], x[0]))
    for i in range(n):
        print(result[i][0], end = ' ')