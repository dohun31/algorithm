from itertools import product
import sys
sys.setrecursionlimit(10*6)
n, k = map(int, sys.stdin.readline().split())
nums = set(list(map(int, sys.stdin.readline().split())))

max_num = 0 # max_num 기록
for i in range(2):
    for num_set in product(nums, repeat=len(str(n)) - i):
        num = int(''.join(map(str, num_set))) # 뽑은 숫자들을 합쳐서 숫자로 바꿈
        if num > n: # n보다 크면 무시
            continue
        else:
            max_num = max(max_num, num)
print(max_num)