if __name__ == "__main__":
    import sys
    from itertools import combinations
    input = sys.stdin.readline

    n, m = map(int, input().split())

    chicken = []
    house = []
    graph = []
    for i in range(n):
        g = list(map(int, input().split()))
        g.append(g)
        for j in range(n):
            if g[j] == 1:
                house.append((i, j))
            elif g[j] == 2:
                chicken.append((i, j))

    min_sum = int(1e10)
    for com in combinations(chicken, m):
        now_sum = 0
        for x1, y1 in house:
            now_sum += min([abs(x1 - x2) + abs(y1 - y2) for x2, y2 in com])
        min_sum = min(min_sum, now_sum)
    print(min_sum)