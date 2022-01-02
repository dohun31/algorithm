def solution(start):
    if len(stack) == M:
        print(*stack)
        return
    for i in range(start, N + 1):
        stack.append(i)
        solution(i)
        stack.pop()
    return

if __name__ == "__main__":
    N, M = map(int, input().split())
    stack = []
    solution(1)