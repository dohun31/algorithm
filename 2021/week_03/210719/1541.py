import sys
datas = sys.stdin.readline().rstrip()
result = []
number = ''

is_minus = False # 처음 마이너스가 나올때를 체크하기 위한 변수
for i in range(len(datas)):
    if datas[i] != '-' and datas[i] != '+': # 연산자가 아니면 이전의 숫자와 합침
        number += datas[i]
    else:
        if is_minus: # 앞에 마이너스가 나왔다면
            result.append(-1 * int(number)) # -1을 곱하고 result에 넣어줌
        else:
            result.append(int(number))
        if not is_minus and datas[i] == '-': # 마이너스가 처음 나왔다면 체크!
            is_minus = True 
        number = ''
# 마지막 숫자를 위한 처리
if is_minus:
    result.append(-1 * int(number))
else:
    result.append(int(number))

print(sum(result))