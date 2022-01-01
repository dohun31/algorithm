def getPrimes(start, end):
    import math
    primes = []
    for number in range(start, end):
        for i in range(2, int(math.sqrt(number))+ 1):
            if number % i == 0:
                break
        else:
            primes.append(number)
    return primes

def solution(number):
    number = str(number)
    for i in range(1, n):
        nowv = int(number[:i])
        if nowv not in check_primes:
            return False
    return True

if __name__ == "__main__":
    n = int(input())
    check_primes = getPrimes(2, 10 ** (n - 1))
    possible_primes = getPrimes(10 ** (n - 1), 10 ** n)
    answers = []
    for prime in possible_primes:
        if solution(prime):
            answers.append(prime)
    for answer in answers:
        print(answer)