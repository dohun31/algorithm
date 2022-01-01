def solution(s):
    answer = 1
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s) + 1):
            nowv = s[i:j]
            if nowv == nowv[::-1]:
                answer = max(answer, len(nowv))
    return answer

if __name__ == "__main__":
    s = "abcdcba"
    print(solution(s))