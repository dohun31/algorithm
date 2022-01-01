def solution(people, limit):
    people.sort()
    answer = 0
    start, end = 0, len(people) - 1
    while start <= end:
        sumv = people[start] + people[end]
        if start != end and sumv <= limit:
            start += 1
        end -= 1
        answer += 1
    return answer

if __name__ == "__main__":
    people = [70, 80, 50, 50]
    limit = 100
    print(solution(people, limit))