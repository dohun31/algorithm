import heapq

def solution(jobs):
    q = [(start + end, (start, end)) for start, end in jobs]
    heapq.heapify(q)
    nowv = heapq.heappop(q)
    answer = nowv[1][1]
    last = nowv[1][1]
    while q:
        nowv = heapq.heappop(q)
        now_len = nowv[1][1]
        if nowv[1][0] <= last:
            now_start = last
        else:
            now_start = last + nowv[1][0] - last
        now_end = now_start + now_len
        answer += now_end - nowv[1][0]
        last = now_end
    return round(answer / len(jobs))

if __name__ == "__main__":
    jobs = [[0, 10], [4, 10], [15, 2], [5, 11]]
    print(solution(jobs))