import sys
numbers = [0] * 10000
for _ in range(int(sys.stdin.readline().rstrip())):
    numbers[int(sys.stdin.readline().rstrip()) - 1] += 1

for i in range(10000):
    if numbers[i] > 0:
        for j in range(numbers[i]):
            print(i + 1)