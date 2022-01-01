array = list(map(int, input()))

#제일 처음 value로 시작
result = array[0]

for i in array[1:]:
    if result <= 1 or i <= 1:
        result += i
    else: result *= i

print(result)