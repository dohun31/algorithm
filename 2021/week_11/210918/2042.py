def init(node, start, end):
    if start == end:
        tree[node] = data[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)
    return tree[node]

def update(node, start, end, target, diff):
    if target < start or target > end:
        return
    tree[node] += diff
    mid = (start + end) // 2
    if start != end:
        update(node * 2, start, mid, target, diff)
        update(node * 2 + 1, mid + 1, end, target, diff)

def query(node, start, end, left, right):
    if left > end or right < start : return 0
    if left <= start and end <= right: return tree[node]
    mid = (start + end) // 2
    return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n, m, k = map(int, input().rstrip().split())
    data = [int(input()) for _ in range(n)]
    tree = [0] * (n * 4)
    # Segment Tree init
    init(1, 0, n - 1)
    for _ in range(m + k):
        a, b, c = map(int, input().rstrip().split())
        b -= 1
        if a == 1:
            diff = c - data[b]
            data[b] += diff
            update(1, 0, n - 1, b, diff)
        elif a == 2: print(query(1, 0, n - 1, b, c - 1))