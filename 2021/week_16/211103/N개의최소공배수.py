def is_prime(number):
    import math
    if number == 1:
        return False
    for i in range(2, int(math.sqrt(number))+ 1):
        if number % i == 0:
            return False # 소수가 아님
    return True # 소수임

def find_div(arr, primes):
    possible = 0
    for prime in primes:
        cnt = 0
        for idx, number in enumerate(arr):
            if number % prime != 0: continue
            else:
                cnt += 1
                number = number // prime
            arr[idx] = number
        if cnt != 0:
            possible = prime
            break
    return possible, arr

def solution(arr):
    answer = 1
    prime = [i for i in range(1, 101) if is_prime(i)]
    while True:
        possible, next_arr = find_div(arr, prime)
        if not possible:
            break
        answer *= possible
        arr = next_arr
    for number in arr:
        answer *= number
    return answer

if __name__ == "__main__":
    arr = [60, 40, 48]
    print(solution(arr))