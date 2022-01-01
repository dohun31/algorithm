def solution(N):
    answer = 0
    while N > 0:
        if N % 2 == 1:
            answer += 1
            N -= 1
        if N % 2 == 0:
            N /= 2
    return answer

if __name__ == "__main__":
    N = 5000
    print(solution(N))