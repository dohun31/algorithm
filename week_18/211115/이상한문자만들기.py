def solution(s):
    answer, idx = '', 0
    for c in s:
        if c == ' ': idx = 0
        else:
            if idx % 2 == 0: c = c.upper()
            else: c = c.lower()
            idx += 1
        answer += c
    return answer

if __name__ == "__main__":
    s = "ab ab ab ab"
    print(solution(s))