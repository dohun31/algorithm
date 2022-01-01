import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)][::-1] # 삼각형 뒤집기

for i in range(1, n): # 좌, 우 중에 제일 큰값 더해서 올라가기
    for j in range(len(graph[i])):
        graph[i][j] += max(graph[i - 1][j], graph[i - 1][j + 1])

print(*graph[-1])