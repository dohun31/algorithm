import sys
points = [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
for point in sorted(points, key=lambda x:(x[1], x[0])):
    print(point[0], point[1])