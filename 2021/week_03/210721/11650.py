import sys
points = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(int(sys.stdin.readline().rstrip()))]
for point in sorted(points, key=lambda x:(x[0], x[1])):
    print(point[0], point[1])