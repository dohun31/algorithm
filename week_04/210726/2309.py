datas = [int(input()) for _ in range(9)]

datas_sum = sum(datas)

for i in range(9):
    for j in range(i + 1, 9):
        if 100 == datas_sum - (datas[i] + datas[j]):
            num1, num2 = datas[i], datas[j]
            datas.remove(num1)
            datas.remove(num2)
            datas.sort()
            print('\n'.join(map(str, datas)))
            break
    if len(datas) < 9:
        break