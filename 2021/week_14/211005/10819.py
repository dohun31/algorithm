if __name__ == "__main__":
    from itertools import permutations
    import sys
    input = sys.stdin.readline

    n = int(input())
    datas = list(map(int, input().split()))

    sumv = 0
    for per in permutations(datas, n):
        now_sumv = 0
        for i in range(n - 1):
            now_sumv += abs(per[i] - per[i + 1])
        sumv = max(sumv, now_sumv)
    print(sumv)