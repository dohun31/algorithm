import sys

multi = 1
for _ in range(3):
    # 차례대로 3개의 숫자를 곱함
    multi *= int(sys.stdin.readline().rstrip())

for i in range(10):
    print(str(multi).count(str(i)))

#numbers = [0] * 10

# for number in str(multi):
#     numbers[int(number)] += 1


# for number in numbers:
#     print(number)

