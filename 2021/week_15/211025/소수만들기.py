def is_prime(n):
    import math
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+ 1):
        if n % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(nums):
    from itertools import combinations
    count = 0
    for num in combinations(nums, 3):
        if is_prime(sum(num)):
            count += 1
    return count

if __name__ == "__main__":
    nums = [1,2,7,6,4]
    print(solution(nums))