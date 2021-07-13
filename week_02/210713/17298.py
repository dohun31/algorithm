import sys

N = int(input())
datas = list((map(int, sys.stdin.readline().split())))
stack = []
result = [-1] * N

stack.append(0)
for i in range(1, N):
    while stack and datas[stack[-1]] < datas[i]:
        result[stack.pop()] = datas[i]
    stack.append(i)
    print(stack)
print(*result)