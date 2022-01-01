import sys

N = int(input())

hi = [0]
print(hi[0:0] + [1, 2, 3])


for _ in range(N):
    datas = sys.stdin.readline().rstrip()
    stack = []
    index = 0
    for data in datas:
        if data == '<':
            if index > 0:
                index -= 1
            else:
                continue
        elif data == '>':
            if (stack or index != 0) and len(stack) > index:
                index += 1
            else:
                continue
        elif data == '-':
            if stack:
                index -= 1
                if index >= 0:
                    stack = stack[:index] + stack[index + 1:]
            else:
                continue
        else:
            stack = stack[:index] + [data] + stack[index:]
            index += 1
        if index < 0:
            index = 0
    print("".join(stack))