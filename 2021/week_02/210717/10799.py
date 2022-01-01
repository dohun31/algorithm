import sys

datas = sys.stdin.readline().rstrip()
stack = []
count = 0

for i in range(len(datas)):
    if datas[i] == '(':
        stack.append(datas[i])
    else:
        stack.pop()
        if datas[i - 1] == '(':
            count += len(stack)
        elif datas[i - 1] == ')':
            count += 1

print(count)