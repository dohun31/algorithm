import sys
datas = list(sys.stdin.readline().rstrip())
stack = []
result = ''

for data in datas:
    if stack and stack[-1] == '<':
        if data == '>':
            stack.pop()
        result += data
    else:
        if data == ' ' or data == '<':
            data == '<' and stack.append(data)
            while stack:
                result += stack.pop()
            result += data
        else:
            stack.append(data)

while stack:
    result += stack.pop()
# 공백이나 < 앞에선 하나의 문자열
# <열리면 >닫힐때까지 넣기
print(result)