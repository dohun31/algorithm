from collections import Counter
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    numbers = Counter([int(sys.stdin.readline()) for _ in range(n)])
    print(sorted(numbers.most_common(), key = lambda x: (-x[1], x[0]))[0][0])