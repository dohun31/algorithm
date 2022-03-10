from math import ceil
import sys

if __name__ == "__main__":
    a, b, v = map(int, sys.stdin.readline().split())

    print(ceil((v - a) / (a - b)) + 1)