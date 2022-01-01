import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7

def solution(scoville, K):
    heapq.heapify(scoville)
    result = 0
    while scoville[0] <= K:
        if len(scoville) > 1:
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
            result += 1
        else:
            return -1
    return result

print(solution(scoville, K))