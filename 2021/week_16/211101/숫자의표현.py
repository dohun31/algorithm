def solution(n):
    number = [i for i in range(1, n + 1)]
    answer = 0
    end = 0
    sumv = number[0]
    for start in range(n):
        while end <= n - 2 and sumv + number[end + 1] <= n:
            end += 1
            sumv += number[end]
        if sumv == n:
            answer += 1
        sumv -= number[start]
    return answer

if __name__ == "__main__":
    n = 15
    print(solution(n))