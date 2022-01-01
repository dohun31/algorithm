import sys
numbers = list(sys.stdin.readline().rstrip())
stack = []

num = ''
for number in numbers:
    if not stack:
        stack.append(number)
    else:
        if int(number) - int(stack[-1]) == 1:
            stack.append(number)
        else:
            if num:
                if int(num) - int(stack[-1]) == 1:
                    stack.append(num)
        