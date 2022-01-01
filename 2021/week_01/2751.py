N = input()

answer = ''

for number in reversed(sorted(N)):
    answer += number

print(answer)
