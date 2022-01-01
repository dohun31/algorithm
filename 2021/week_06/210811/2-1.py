def solution(n):
    i = n + 1; one_cnt = list(format(n, 'b')).count('1')
    while True: 
        if list(format(i, 'b')).count('1') == one_cnt:
            return i
        i += 1
print(solution(78))

def solution1(numbers):
    zero, non_zero = [], []
    for i in numbers: 
        if i % 10 == 0: zero.append(str(i))
        else: non_zero.append(str(i))
    return ''.join(sorted(non_zero, reverse=True)) + ''.join(sorted(zero, reverse=True))
print(solution1([412, 41]))