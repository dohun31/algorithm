def solution(dartResult):
    score, bonus, num = [], {"S": 1, "D": 2, "T": 3}, ''
    for c in dartResult:
        if c.isdigit(): num += c
        else:
            if num: score.append(int(num)); num = ''
            if bonus.get(c, 0): score[-1] = score[-1] ** bonus[c]
            elif c == '*':
                score[-1] *= 2
                if len(score) > 1: score[-2] *= 2
            else: score[-1] = -score[-1]
    return sum(score)

if __name__ == "__main__":
    dartResult = "1D2S3T*"
    print(solution(dartResult))