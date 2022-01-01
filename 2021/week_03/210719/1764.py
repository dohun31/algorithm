import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().split())
listen = Counter(sys.stdin.readline().rstrip() for _ in range(N)) # 듣지도 못한 사람
see = Counter(sys.stdin.readline().rstrip() for _ in range(M)) # 보지도 못한 사람
names = []

for item in list((listen + see).items()): # 듣지도 or 보지도 의 itmes를 탐색
    if item[1] > 1: # 만약에 듣지도 보지도 못했을 경우 item은 1보다 크다
        names.append(item[0])

print(len(names))
for name in sorted(names):
    print(name)