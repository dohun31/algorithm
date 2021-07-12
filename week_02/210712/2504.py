import sys

datas = sys.stdin.readline().strip()

stack = []
flag = True # 괄호 쌍 확인하는 변수

def solution(number):
    now_x = '('
    now_sum = 1
    if number == 3:
        now_x = '['
    # 스택이 비어있지 않고, 젤 위의 값이 숫자라면
    if stack and str(stack[-1]).isdigit():
        now_sum = 0
        while stack and str(stack[-1]).isdigit():
            now_sum += stack.pop() # 다 더하고
    # 괄호 한 쌍이 만들어진다면
    if stack and stack[-1] == now_x:
        stack.pop() 
        stack.append(number * now_sum) # 결과를 스택에 push해줌 
        # 앞에 정수가 있었다면 now_sum > 1 이고, 아니라면 1이어서 그냥 number를 push하는것과 동일함
    else:
        return False # 괄호 한 쌍이 만들어지지 않으면 False를 반환
    return True

for data in datas:
    # 여는 괄호일 경우 무조건 스택에 삽입,
    if data == '(' or data == '[':
        stack.append(data)
    # 닫는 괄호의 경우
    elif data == ')':
        result = solution(2)
        if not result:
            flag = False
            break
    elif data == ']':
        result = solution(3)
        if not result:
            flag = False
            break

# flag가 True이고 남아있는 괄호가 없다면
if flag and str(stack[0]).isdigit():
    # stack에 들어가 있는 모든 정수의 합을 출력
    print(sum(stack))
# 이외의 경우는 모두 0 출력
else:
    print(0)