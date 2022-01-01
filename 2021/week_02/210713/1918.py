datas = input()
stack = []
result = ""

for data in datas:
    # +나 -는 앞에꺼 상관없이 그냥 (있다면 ( 전까지, 아니면 스택이 빌 때 까지 pop
    if data == '+' or data == '-':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(data)
    # * / 는 일단 push하는데 만약에 스택에 *나 /가 있으면 pop
    elif data == '*' or data == '/':
        if stack and (stack[-1] == '*' or stack[-1] =='/'): 
            result += stack.pop()
        stack.append(data)
    # (는 무조건 push
    elif data == '(':
        stack.append(data)
    # )는 (나올때까지 pop
    elif data == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()
    # 문자들은 들어오면 바로 출력
    else:
        result += data

while stack:
    result += stack.pop()

print(result)