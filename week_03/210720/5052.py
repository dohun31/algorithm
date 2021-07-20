import sys

n = int(input())
for _ in range(n):
    N = int(input())
    calls = [sys.stdin.readline().rstrip() for _ in range(N)]
    calls.sort()
    flag = True
    for i in range(N - 1):
        if calls[i] == calls[i + 1][:len(calls[i])]:
            flag = False
            break
    print("YES" if flag else "NO")