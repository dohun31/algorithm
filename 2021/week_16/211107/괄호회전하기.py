def check(s):
    stack, cnt = [], 0
    for c in s:
        if c in '[{(':
            stack.append(c)
        else:
            if c == ']':
                target = '['
            elif c == '}':
                target = '{'
            elif c == ')':
                target = '('
            if stack and stack[-1] == target:
                stack.pop()
            else:
                return False, 0
            if not stack:
                cnt += 1
    if stack: 
        return False, 0
    else: 
        return True, cnt

def solution(s):
    answer = 0
    for _ in range(len(s)):
        a, answer = check(s)
        if a:
            break
        else:
            s = s[1:] + s[0]
    return answer

if __name__ == "__main__":
    s = "}]()[{"
    print(solution(s))