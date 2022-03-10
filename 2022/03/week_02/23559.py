import sys
sys.setrecursionlimit(10**9)

def get_max_value(idx, value, nowx):
    if nowx < 0:
        return 0
    next_idx = idx + 1
    if next_idx == n:
        return value
    return value + max(get_max_value(next_idx, arr_a[next_idx], nowx - 5000), get_max_value(next_idx, arr_b[next_idx], nowx - 1000))

if __name__ == "__main__":
    n, x = map(int, sys.stdin.readline().split())
    arr_a = []
    arr_b = []

    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        arr_a.append(a)
        arr_b.append(b)

    result = max(get_max_value(0, arr_a[0], x - 5000), get_max_value(0, arr_b[0], x - 1000))
    print(result)
