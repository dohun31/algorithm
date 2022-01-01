def solution(food_times, k):
    import heapq
    q = [[food, i] for i, food in enumerate(food_times)]
    heapq.heapify(q)
    cnt , min_food = 0, 0
    while q:
        if cnt + (q[0][0] - min_food) * len(q) <= k:
            cnt += (q[0][0] - min_food) * len(q)
            min_food, _ = heapq.heappop(q)
        else:
            break
    if not q:
        return -1
    else:
        return sorted(q, key=lambda x: (x[1]))[(k  - cnt) % len(q)][1] + 1

food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))