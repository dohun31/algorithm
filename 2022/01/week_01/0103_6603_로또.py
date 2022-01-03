def lotto(start):
    if len(stack) == 6:
        print(*stack)
        return
    for i in range(start, k):
        if s[i] not in stack:
            stack.append(s[i])
            lotto(i + 1)
            stack.pop()

if __name__ == "__main__":
    stack = []
    while True:
        args = list(map(int, input().split()))
        k = args[0] # 집합 크기
        if k == 0:
            break
        s = args[1:] # 숫자 집합
        lotto(0)
        print()