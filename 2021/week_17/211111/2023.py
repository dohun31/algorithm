def is_prime(number):
    import math
    for i in range(2, int(math.sqrt(number))+ 1):
        if number %  i == 0:
            return False
    return True

def solution(number):
    if len(number) == n:
        print(number)
        return True
    for i in range(1, 10):
        now_number = number + str(i)
        if is_prime(int(now_number)):
            solution(now_number)

if __name__ == "__main__":
    n = int(input())
    start = ['2', '3', '5', '7']
    for i in start:
        solution(i)