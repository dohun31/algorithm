import sys

N = int(input())
datas = list((map(int, sys.stdin.readline().split())))
stack = [] # 인덱스들 저장하는 스택
result = [-1] * N # 결과 저장하는 스택

stack.append(0)
for i in range(1, N):
    # datas[stack[-1]] 보다 datas[i]가 크면
    while stack and datas[stack[-1]] < datas[i]:
        # result[stack.pop()] 을 갱신
        result[stack.pop()] = datas[i]
    # 다음 인덱스 스택에 삽입
    stack.append(i)
print(*result)