def solution(n, left, right):
    return [max(i // n, i % n) + 1 for i in range(left, right + 1)]

if __name__ == "__main__":
    n = 3
    left = 2
    right = 5
    print(solution(n, left, right))