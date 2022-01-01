def solution(N, stages):
    n = len(stages)
    result = []
    for i in range(1, N + 1):
        cnt = stages.count(i)
        result.append({'n': i, 'c': cnt / n if n > 0 else 0})
        n -= cnt
    return [i['n'] for i in sorted(result, key=lambda x:(-x['c'], x['n']))]

N = 5
stages = [4,4,4,4,4]
print(solution(N, stages))