def solution(citations):
    answer = len(citations)
    for i, citation in enumerate(sorted(citations, reverse = True)):
        if (i + 1) >= citation:
            answer = i
            break
    return answer

if __name__ == "__main__":
    citations = [0,1,2,3,3,3,3,3,3,4,10,20,30,40]
    print(solution(citations))