from collections import deque

def show():
    print("---------")
    for g in graph:
        print(g)
    print('---------')

def play(start, now_direction, now_change_info, time):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pointer = [(2, 3), (3, 2), (1, 0), (0, 1)]

    target_time, target_direction = now_change_info
    di, dj = direction[now_direction]
    nowi, nowj = start

    while time <= int(target_time):
        ni, nj = nowi + di, nowj + dj
        if 0 <= ni < n and 0 <= nj < n:
            if graph[ni][nj] == 0:
                li, lj = path.popleft()
                graph[li][lj] = 0
            elif graph[ni][nj] == 1:
                return time
            elif graph[ni][nj] == 2:
                graph[ni][nj] = 0
            graph[ni][nj] = 1
            path.append((ni, nj))
        else:
            return time
        show()
        nowi, nowj = ni, nj
        time += 1
    if change_info:
        next = change_info.popleft()
    else:
        next = ['10000', 'D']
    return play((nowi, nowj), pointer[now_direction][target_direction == 'D'], next, time)

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    change_info = deque()

    for _ in range(k):
        row, col = map(lambda x: int(x) - 1, input().split())
        graph[row][col] = 2
    
    for _ in range(int(input())):
        change_info.append(input().split())

    graph[0][0] = 1
    path = deque([(0, 0)])
    print(play((0, 0), 3, change_info.popleft(), 1))