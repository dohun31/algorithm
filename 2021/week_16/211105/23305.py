if __name__ == "__main__":
    from collections import defaultdict

    n = int(input())
    want_class = defaultdict(list)
    now_data = list(map(int, input().split()))
    want_data = list(map(int, input().split()))
    for i in range(n):
        want_class[want_data[i]].append(now_data[i])
    want_class = sorted(want_class.items(), key = lambda x: x[0])
    print(want_class)