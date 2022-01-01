import heapq

def solution(n, works):
    q = []
    for work in works:
        heapq.heappush(q, (-work, work))
    while q and n:
        nowv = heapq.heappop(q)[1] - 1
        if nowv != 0:
            heapq.heappush(q, (-nowv, nowv))
        n -= 1
    return sum([work ** 2 for _, work in q])

if __name__ == "__main__":
    works = [1, 1]
    n = 3
    print(solution(works, n))