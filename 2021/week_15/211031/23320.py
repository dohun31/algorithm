if __name__ == "__main__":
    N = int(input())
    datas = list(map(int, input().split()))
    X, Y = map(int, input().split())

    a = int(N * X / 100)
    b = 0
    for data in sorted(datas, reverse=True):
        if data >= Y: b += 1
        else: break
    
    print(a, b)