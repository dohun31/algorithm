import sys
from collections import Counter
N, M = map(int, sys.stdin.readline().split())
# A, B를 counter로 만듦
A = Counter(list(map(int, sys.stdin.readline().split())))
B = Counter(list(map(int, sys.stdin.readline().split())))

print(len(A - B) + len(B - A))
