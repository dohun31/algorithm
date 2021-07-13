datas = input()
stack = []
result = ""

def pop_all():
    global result
    while stack and stack[-1] != '(':
        result += stack.pop()

for data in datas:
    if data == '+' or data == '-':
        pop_all()
        stack.append(data)
    elif data == '*' or data == '/':
        if stack and (stack[-1] == '*' or stack[-1] =='/'): 
            result += stack.pop()
        stack.append(data)
    elif data == '(':
        stack.append(data)
    elif data == ')':
        pop_all()
        stack.pop()
    else:
        result += data

while stack:
    result += stack.pop()
print(result)