import sys
from collections import deque
from itertools import product

n = int(input())
operator = ['+', '-', '*', '/']
nums = [list(map(int, input().split()))]

my_operator = []
for idx, op in enumerate(map(int, input().split())):
    if op >= 1:
        for i in range(op):
            my_operator.append(operator[idx])

max = -10**9
min = 10**9
for set in product(my_operator, repeat=n):
    sum = nums[0]
    idx = 0
    q = deque(set)
