import sys

N = int(sys.stdin.readline())
p_numbers = [] # positive 
n_numbers = [] # negative
z_numbers = [] # zero
p_result = [] # positive max_sum
n_result = [] # negative max_sum

for _ in range(N):
    number = int(sys.stdin.readline())
    if number < 0:
        n_numbers.append(number)
    elif number > 0:
        p_numbers.append(number)
    else:
        z_numbers.append(number)

p_numbers.sort(reverse = True)
n_numbers.sort()
if len(n_numbers) % 2 != 0 and z_numbers:
    n_numbers.pop()

flag = True
for number in p_numbers:
    if number != 1:
        if p_result:
            if flag:
                p_result.append(number * p_result.pop())
                flag = not flag
            else:
                p_result.append(number)
                flag = not flag
        else:
            p_result.append(number)
    else:
        p_result.append(number)

flag = True
for number in n_numbers:
    if n_result:
        if flag:
            n_result.append(number * n_result.pop())
            flag = not flag
        else:
            n_result.append(number)
            flag = not flag
    else:
        n_result.append(number)

print(sum(p_result) + sum(n_result))