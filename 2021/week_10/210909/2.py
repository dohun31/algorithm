directions = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}

def find_dict(dict, d):
    if dict == (-1, 0): return (0, -1) if d == 'L' else ((0, 1) if d == 'R' else 0)
    elif dict == (1, 0): return (0, 1) if d == 'L' else ((0, -1) if d == 'R' else 1)
    elif dict == (0, -1): return (1, 0) if d == 'L' else ((-1, 0) if d == 'R' else 2)
    elif dict == (0, 1): return (-1, 0) if d == 'L' else ((1, 0) if d == 'R' else 3)

def solution(grid):
    def dfs(x, y, dict, cnt):
        # dx, dy 구하기
        if grid[x][y] == 'S': dx, dy = dict[0], dict[1]
        elif grid[x][y] == 'L': dx, dy = find_dict(dict, 'L')
        elif grid[x][y] == 'R': dx, dy = find_dict(dict, 'R')
        # 방향 번호 체크
        dnum = find_dict((dx, dy), '')
        # 이전에 지나간 방향이라면 이제 끝
        if dnum in visited[x][y]:
            return cnt
        # 지나가는 방향 표시
        visited[x][y].append(dnum)
        nx, ny = (x + dx) % lr, (y + dy) % lc
        return dfs(nx, ny, (dx, dy), cnt + 1)
    # 
    lr, lc = len(grid), len(grid[0])
    grid = list(map(list, grid))
    answer, tmp = [], []
    for i in range(4):
        visited = [[[] for _ in range(lc)] for _ in range(lr)]
        visited[0][0].append(i)
        nx, ny = (0 + directions[i][0]) % lr, (0 + directions[i][1]) % lc
        cnt = dfs(nx, ny, directions[i], 1)

        for i in range(len(visited)):
            for j in range(len(visited[i])):
                visited[i][j] = sorted(visited[i][j])

        c = 0
        for t in tmp:
            if t == visited: break
            else: c += 1
        if c == len(tmp): tmp.append(visited); answer.append(cnt)
        
    return answer


grid = ["R","R"]
print(solution(grid))