import sys
data = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
stack = []

for i in range(len(data)):
    stack.append(data[i])
    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
            if ''.join(stack[-len(bomb):]) == bomb:
                for _ in range(len(bomb)):
                    stack.pop()
    
print(''.join(stack) if stack else 'FRULA')