import sys
import heapq

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        k = int(sys.stdin.readline())
        q = []
        for _ in range(k):
            cmd = sys.stdin.readline().rstrip().split()
            cmd[1] = int(cmd[1])
            if cmd[0] == 'I':
                heapq.heappush(q, cmd[1])
            elif cmd[0] == 'D' and q:
                if cmd[1] == 1:
                    q = heapq.nlargest(len(q), q)[1:]
                else:
                    q = heapq.nsmallest(len(q), q)[1:]
            print(q)
        if not q:
            print('EMPTY')
        else:
            print(q[-1], q[0])