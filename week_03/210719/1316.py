import sys
N = int(sys.stdin.readline().rstrip())
count = 0

for _ in range(N):
    dict ={}
    flag = True
    data = sys.stdin.readline().rstrip()
    for i in range(len(data)):
        if dict.get(data[i]): # 이전에 나온 알파벳인데
            # 앞이랑 다르다면? 이때 data[i - 1] null 체크 필요 없음. 
            # get에 뭐가 있다는거 자체가 이미 data[0]에서 벗어난것
            if data[i] != data[i - 1]: 
                flag = False
                break
        else:
            dict[data[i]] = True
    if flag:
        count += 1

print(count)