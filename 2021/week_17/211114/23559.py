if __name__ == "__main__":
    import heapq
    n, x = map(int, input().split())
    answer, q = 0, []
    for _ in range(n):
        a, b = map(int, input().split())
        heapq.heappush(q, (-a, -b))
    while q:
        a, b = heapq.heappop(q)
        if x >= 5000:
            if a < b:
                answer -= a
                x -= 5000
            else:
                answer -= b
                x-= 1000
        elif x >= 1000:
            answer -= b
            x -= 1000
    print(answer)