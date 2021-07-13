N = int(input())

for _ in range(N):
    left_stack = [] # 커서 왼쪽을 담을 스택
    right_stack = [] # 커서 오른쪽을 담을 스택
    datas = input()
    for data in datas:
        if data == "-" and left_stack: # - 이고 커서 왼쪽에 값이 존재한다면
            left_stack.pop() # 문자 하나 제거
        elif data == "<" and left_stack: # < 이고 커서 왼쪽에 값이 존재한다면
            right_stack.append(left_stack.pop()) # 커서를 왼쪽으로 하나 옮김 -> 왼쪽의 값을 커서 오른쪽으로 이동
        elif data == ">" and right_stack: # > 이고 커서 오른쪽에 값이 존재한다면
            left_stack.append(right_stack.pop()) # 커서를 오른쪽으로 하나 옮김 -> 오른쪽의 값을 커서 왼쪽으로 이동
        else: # 문자의 경우
            left_stack.append(data) # 커서 왼쪽에 삽입
    left_stack.extend(reversed(right_stack)) # reversed 하고 extend함 (커서 오른쪽 값이 right_stack의 제일 위에 있음)
    print("".join(left_stack))
