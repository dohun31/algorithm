def solution():
    if len(stack) == m:
        print(*stack)
        return
    for i in range(n):
        if args[i] not in stack:
            stack.append(args[i])
            solution(i + 1)
            stack.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    args = sorted(list(map(int, input().split())))
    stack = []
    solution(0)