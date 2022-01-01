import sys
from collections import deque

N = int(sys.stdin.readline())
deq = deque()

for _ in range(N):
    data = sys.stdin.readline().split()

    if data[0] == 'push_front':
        deq.appendleft(data[1])
    elif data[0] == 'push_back':
        deq.append(data[1])
    elif data[0] == 'pop_front':
        if len(deq) > 0:
            print(deq.popleft()) 
        else:
            print(-1)
    elif data[0] == 'pop_back':
        if len(deq) > 0:
            print(deq.pop())
        else:
            print(-1)
    elif data[0] == 'size':
        print(len(data[0]))
    elif data[0] == 'empty':
        if len(data) == 0:
            print(1)
        else:
            print(0)
    elif data[0] == 'front':
        if len(data) > 0:
            print(deq[0])
        else:
            print(-1)
    elif data[0] == 'back':
        if len(data) > 0:
            print(deq[-1])
        else:
            print(-1)
    print(deq)
