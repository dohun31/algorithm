scores = [[75, 50, 100], [75, 100, 20], [100, 100, 20]]	

def solution(scores):
    answer, n= '', len(scores)
    scores, grade = [list(x) for x in zip(*scores)], ['F', 'F', 'F', 'F', 'F', 'D', 'D', 'C', 'B', 'A']
    for i, s in enumerate(scores):
        _sum, count = sum(s), n
        if (s[i] == min(s) or s[i] == max(s)) and s.count(s[i]) == 1:
            _sum -= s[i]
            count -= 1
        answer += grade[int((_sum / count) // 10)]
    return answer

print(solution(scores))