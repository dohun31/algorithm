def solution(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse = True))])

if __name__ == "__main__":
    A = [1, 4, 2]
    B = [5, 4, 4]
    print(solution(A, B))