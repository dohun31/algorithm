data = input()
length = len(data)

sum = 0

for i in range(length // 2):
    sum += int(data[i])

for i in range(length // 2, length):
    sum -= int(data[i])

if sum == 0:
    print("LUCKY")
else:
    print("READY")
