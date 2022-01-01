def solution(s, n):
    UPPER, LOWER, ALPHA = 65, 97, 26
    answer = ''
    for c in s:
        if c.isalpha():
            nowv = LOWER
            if c == c.upper(): nowv = UPPER
            c = chr((ord(c) + n - nowv) % ALPHA + nowv)
        answer += c
    return answer


if __name__ == "__main__":
    s = "a B z"
    n = 4
    print(solution(s, n))