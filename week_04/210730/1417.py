import sys
n = int(sys.stdin.readline())
dasom = int(sys.stdin.readline())
other = sorted([int(sys.stdin.readline()) for _ in range(n - 1)], reverse = True) if n > 1 else [0]

count = 0
while dasom <= other[0]:
    other[0] -= 1
    dasom += 1
    count += 1
    other.sort(reverse=True)

print(count)