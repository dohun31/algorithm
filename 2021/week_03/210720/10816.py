import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
dict = Counter(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
result = []
for i in list(map(int, sys.stdin.readline().rstrip().split())):
    # 딕서녀리에 원하는 애들 있으면 그대로 push하고 아니면 default값으로 설정한 0 push
    result.append(dict.get(i, 0))
print(*result)