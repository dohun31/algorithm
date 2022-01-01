from itertools import permutations

def is_prime(number):
    import math
    if number == 1:
        return False
    for i in range(2, int(math.sqrt(number))+ 1):
        if number % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(numbers):
    stack = []
    answer = []
    # 소수 찾기
    for n in range(1, len(numbers) + 1):
        stack += list(permutations(numbers, n))
    stack = [int(''.join(number)) for number in stack]
    # 만들 수 있는 소수 찾기
    for number in stack:
        if number < 2:
            continue
        if is_prime(number): answer.append(number)
    return len(set(answer))

if __name__ == "__main__":
    numbers = "110"
    print(solution(numbers))