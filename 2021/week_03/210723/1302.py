import sys
from collections import Counter
N = int(sys.stdin.readline())
books = Counter(sorted(sys.stdin.readline().rstrip() for _ in range(N)))
print(books.most_common(1)[0][0]) # 제일 많이 읽은 책 중에 처음꺼