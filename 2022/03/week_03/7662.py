import sys
import heapq

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        k = int(input())
        minhq = []
        maxhq = []
        
        for _ in range(k):
            command = input().split()
            num = int(command[1])
            if command[0] == 'I':
                minhq.append(num)
                minhq.append(-num)
            else:
                if num == 1:
                    