import heapq

if __name__ == "__main__":
    n = int(input())
    q = []

    for _ in range(n):
        for num in list(map(int, input().split())):
            heapq.heappush(q, -num)
    
    for _ in range(n - 1):
        heapq.heappop(q)
    
    print(-heapq.heappop(q))