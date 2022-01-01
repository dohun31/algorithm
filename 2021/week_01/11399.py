N = int(input())

array = list(map(int, input().split()))

array.sort()

result = 0

for index, value in enumerate(array):
    result += (N - index) * value

print(result)
    