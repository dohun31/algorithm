def check(num):
    l = len(num)
    for i in range((len(num) + 1) // 2):
        if num[i] != num[l - i - 1]:
            return False
    return True

if __name__ == "__main__":
    while True:
        num = input()
        if num == '0':
            break
        else:
            print(check(num))
