import sys
N = int(sys.stdin.readline())
list_numbers = list(map(int, sys.stdin.readline().split()))
dict_numbers = {}

for number in list_numbers:
    dict_numbers[number] = 0
for index, number in enumerate(sorted(dict_numbers)):
    dict_numbers[number] = index
result = ''
for number in list_numbers:
    print(dict_numbers[number], end=" ")