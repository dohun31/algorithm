def check_all(l, num):
    start = 0
    for k in range(1, l // 2 + 1):
        if num[-k:] == num[-(k*2):-k]:
            return False
        start += 1
    return True

def check_good_number(num, n):
    l = len(num)
    # 원하는 길이라면 return
    if l == n:
        print(num)
        exit()
    # 1, 2, 3하나씩 붙이기
    for i in '123':
        number = num + i
        if check_all(l + 1, number):
            check_good_number(number, n)

if __name__ == "__main__":
    n = int(input())
    print(check_good_number('', n))