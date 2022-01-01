def solution(A, B):
    A.sort()
    B.sort()
    answer, i, j = 0, 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
            j += 1
            answer += 1
        else:
            j += 1
    return answer

if __name__ == "__main__":
    A = [5, 1, 3, 7]
    B = [2, 2, 6, 8]
    print(solution(A, B))