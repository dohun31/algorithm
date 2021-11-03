def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
    return False if stack else True

if __name__ == "__main__":
    s = "()()"
    print(solution(s))