import sys
input = sys.stdin.readline
cnt = 1

while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    max = l * (v // p) + (v % p if v % p <= l else l)
    print(f"Case {cnt}: {max}")
    cnt += 1