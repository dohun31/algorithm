import sys

def solution(a, b, c):
    a, b, c = sorted([a, b, c])
    return "right" if a ** 2 + b ** 2 == c ** 2 else "wrong"

if __name__ == "__main__":
    while True:
        a, b, c = map(int, sys.stdin.readline().split())
        if a == b == c == 0:
            break
        print(solution(a, b, c))