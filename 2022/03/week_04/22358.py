import sys
import heapq

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    
    left_q, right_q = [], []
    target_num = None

    for _ in range(n):
        num = int(sys.stdin.readline())
        if target_num == None:
            target_num = num
        else:
            if target_num > num:
                heapq.heappush(left_q, -num)
            else:
                heapq.heappush(right_q, num)
            if len(left_q) - len(right_q) >= 1:
                heapq.heappush(right_q, target_num)
                target_num = -heapq.heappop(left_q)
            elif len(right_q) - len(left_q) > 1:
                heapq.heappush(left_q, -target_num)
                target_num = heapq.heappop(right_q)
        print(target_num)