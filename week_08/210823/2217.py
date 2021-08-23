from collections import Counter
n = int(input())
rope = sorted(Counter([int(input()) for _ in range(n)]).items(), key=lambda x: (x[1], x[0]))

max_weight = 0
l = 0
for weight, cnt in rope:
    max_weight = max(weight * (n - l), max_weight)
    l += cnt

print(max_weight)