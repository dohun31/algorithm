def solution(n):
    number = ['4', '1', '2']
    answer = ''
    while n:
        answer = number[n % 3] + answer
        n = n // 3 - (n % 3 == 0)
    return answer

if __name__ == "__main__":
    n = 8
    print(solution(n))