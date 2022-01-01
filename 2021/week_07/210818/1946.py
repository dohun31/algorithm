import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    scores = [0 for _ in range(n)]
    for _ in range(n):
        s1, s2 = map(int, input().split())
        scores[s1 - 1] = s2

    cnt = 1
    min_interview_sc = scores[0]
    for i in range(1, n):
        if scores[i] < min_interview_sc:
            cnt += 1
            min_interview_sc = scores[i]    

    print(cnt)