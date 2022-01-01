def solution(d, budget):
    d.sort()
    end = 0
    sumv = d[end]
    result = 0
    for start in range(len(d)):
        while end <= len(d) - 2 and sumv + d[end + 1] <= budget:
            end += 1
            sumv += d[end]
        if sumv <= budget:
            result = max(result, end - start + 1)
        sumv -= d[start]
    return result

if __name__ == "__main__":
    d = [11, 12, 13]
    budget = 10
    result = solution(d, budget)
    print(result) 