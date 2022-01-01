directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)} # 상하좌우

def solution(dirs):
    row = col = 11
    nx = ny = 5
    road = []
    for d in dirs:
        dx, dy = directions[d]
        # 범위 밖으로 나가면 취급 x
        if 0 <= nx + dx < row and 0 <= ny + dy < col:
            cx, cy = nx + dx, ny + dy # 이동할 지점
            gp = (nx, ny, cx, cy)
            bp = (cx, cy, nx, ny)
            if gp not in road: 
                road.append(gp)
                road.append(bp)
            nx, ny = cx, cy # 현재 지점 갱신
    return len(road) // 2

if __name__ == "__main__":
    dirs = "LULLLLLLU"
    print(solution(dirs))