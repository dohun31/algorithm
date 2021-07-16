import sys

left_list = list(map(str, sys.stdin.readline().rstrip()))
right_list = []
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    data = sys.stdin.readline().split()
    if data[0] == 'P':
        left_list.append(data[1])
    elif data[0] == 'L':
        left_list and right_list.append(left_list.pop())
    elif data[0] == 'D':
        right_list and left_list.append(right_list.pop())
    elif data[0] == 'B':
        left_list and left_list.pop()
        
left_list.extend(reversed(right_list))
print("".join(left_list))