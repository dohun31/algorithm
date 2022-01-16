import math

def solution(n):
    sqrtv = math.sqrt(n)
    return int(pow(sqrtv + 1, 2)) if int(sqrtv) == sqrtv else -1

print(solution(121))