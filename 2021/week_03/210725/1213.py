import sys
from collections import Counter
datas = Counter(sys.stdin.readline().rstrip())
datas_itmes = sorted(datas.items(), key=lambda x: x[0])
flag = True
result = ''
odd_str = ''

for data in datas_itmes:
    if data[1] % 2 == 1:
        if odd_str: flag = False; break
        else: odd_str = data[0]

if flag:
    for data in datas_itmes:
        result += data[0] * (data[1] // 2)
    print(result + odd_str + result[::-1])
else:
    print("I'm Sorry Hansoo")
    