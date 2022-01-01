import sys
input = sys.stdin.readline
while True:
    numbers = list(map(int, input().split()))
    if len(numbers) == 1:
        break
    n, numbers = numbers[0], sorted(numbers[1:], reverse = True)

    result = [numbers[0::2], numbers[1::2]]

    for num in result: # 제일 높은 자리수에 0 오는거 방지
        if num[-1] == 0:
            i = len(num) - 2 # num[-2]
            while num[i] == 0:
                i -= 1
            num[-1], num[i] = num[i], num[-1]

    for i in range(2): # 각 자리수에 10^j 를 곱해줌
        for j in range(len(result[i])):
            result[i][j] *= 10**j

    print(sum(map(sum, result)))