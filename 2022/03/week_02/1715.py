import sys
import heapq

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    numbers = [int(sys.stdin.readline()) for _ in range(n)]

    heapq.heapify(numbers)

    sumv = 0
    while len(numbers) >= 2:
        a, b = heapq.heappop(numbers), heapq.heappop(numbers)
        sumv += a + b
        heapq.heappush(numbers, a + b)
    print(sumv)
