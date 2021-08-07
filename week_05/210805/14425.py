import sys
n, m = map(int, sys.stdin.readline().split())
list = sorted([sys.stdin.readline().rstrip() for _ in range(n)])
search_list = [sys.stdin.readline().rstrip() for _ in range(m)]

def binary_search(start, end, target):
    global count
    if start > end:
        return
    mid = (start + end) // 2
    if list[mid] == target:
        count += 1
    elif list[mid] > target:
        binary_search(start, mid - 1, target)
    elif list[mid] < target:
        binary_search(mid + 1, end, target)

count = 0
for a in search_list:
    binary_search(0, n - 1, a)
print(count)