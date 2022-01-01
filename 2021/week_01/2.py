data = input()

result = int(data[0])

for i in range(1, len(data)):
    number = int(data[i])
    if number <= 1 or result <= 1:
        result += number
    else:
        result *= number

print(result)