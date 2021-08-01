import sys
n = int(sys.stdin.readline())

count = 1
number = 666
while count < n:
    number += 1 # 숫자 하나 세어 줌
    if '666' in str(number): # 만약에 숫자에 666 세개 이상 포함돼있으면
        count += 1 # 하나 세어 줌

print(number)