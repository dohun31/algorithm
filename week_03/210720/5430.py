import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    p = sys.stdin.readline().rstrip().replace('RR', '')
    n = int(sys.stdin.readline().rstrip())
    numbers = sys.stdin.readline().rstrip()[1:-1].split(',')

    if n == 0:
        numbers = []

    numbers = deque(list(map(int, numbers)))
    flag = True
    left = True
    
    for P in p:
        if P == 'D':
            if numbers:
                if left:
                    numbers.popleft()
                else:
                    numbers.pop()
            else:
                print("error")
                flag = False
                break
        else:
            left = not left

    if not left: numbers.reverse()
    flag and print("[" + ','.join(map(str, numbers)) + "]")