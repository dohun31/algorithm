def make_n_mod(n, k):
    result = ''
    while n > 0:
        n, mod = divmod(n, k)
        result += str(mod)
    return result[::-1]

def is_prime(n):
    import math
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+ 1):
        if n % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(n, k):
    nmod = make_n_mod(n, k)
    cnt = 0
    for i in nmod.split('0'):
        # if i.isdigit():
        if i.isdigit() and is_prime(int(i)):
                cnt += 1
    return cnt

print(solution(110011, 10)) 