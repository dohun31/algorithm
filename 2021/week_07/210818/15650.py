N, M = map(int, input().split())
arr = []  # 출력 내용

def solution(cnt, start):
    if cnt == M:
        print(*arr)
        return
    for i in range(start, N):
        if i + 1 not in arr:
            arr.append(i + 1)
            solution(cnt + 1, i)
            arr.pop()

solution(0, 0)