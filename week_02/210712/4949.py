import sys

while True :
    datas = sys.stdin.readline()
    # 종료 조건 필요
    if datas[0] == '.':
        break
    # 스택 선언
    stack = []
    status = True
    # 문장 탐색
    for data in datas:
        # 만약에 (나 [ 있으면 스택에 push하기
        if data == '(' or data ==  '[':
            stack.append(data)
        
        # 닫는 괄호 체크하기
        elif data == ')': # ( 일 때
            if stack and stack[-1] == '(': # 스택이 비어있지 않고, 마지막에 ( 가 있어야 함
                stack.pop()
            else:
                status = False
                break
        
        elif data == ']': # [ 일 때
            if stack and stack[-1] == '[': # 스택이 비어있지 않고, 마지막에 [ 가 있어야 함
                stack.pop()
            else:
                status = False
                break
    
    if status and not stack: # status가 계속 True고 스택이 비어야함(모든 괄호들이 사용되어야 함)
        print("yes")
    else: # 아니라면 균형잡인 문자열이 아님
        print("no")