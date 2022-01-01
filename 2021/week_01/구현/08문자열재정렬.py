data = list(map(str, input()))
data.sort() # 숫자 다음에 알파벳

sum = 0 # 숫자 합
last_num = 0 # 첫번째 알파벳 위치 기억

for i in range(len(data)):
    if data[i].isdigit():
        sum += int(data[i])
        last_num += 1
    else:
        break

print(''.join(data[last_num:]) + str(sum))

# K1KA5CB7