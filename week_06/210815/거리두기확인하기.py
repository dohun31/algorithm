import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

def solution(places):
    # 거리 두기 확인하기 
    def bfs(x, y):
        q = deque([(x, y)])
        visited[x][y], mh_checked[x][y] = True, 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            cx, cy = q.popleft()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                    if place[nx][ny] != 'X':
                        mh = abs(x - nx) + abs(y - ny) # 파티션이 아니면 맨해튼 거리 계산
                        mh_checked[nx][ny], visited[nx][ny] =  mh, True # 맨해튼 거리 갱신, 나 들렸어요
                        if place[nx][ny] == 'P' and -1 < mh <= 2: # 사람인데 맨해튼 거리 2 이하이면 신고
                            return 0
                        if mh <= 1: # 맨해튼 거리 1이하일때만 q에 넣음 -> 큐에서 꺼낼때 + 1 되니까 결국엔 거리가 2인애들까지임
                            q.append((nx, ny))
        return 1
    # 탐색 하기
    answer = []
    for place in places: # 5개 구역 돌기
        flag = 1 
        visited = [[False for _ in range(5)] for _ in range(5)] # 방문 체크
        mh_checked= [[-1 for _ in range(5)] for _ in range(5)] # 맨해튼 거리 체크
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P' and not visited[i][j]: # 사람이고 방문 안했으면 bfs 돌기
                        flag = min(bfs(i, j), flag) # 만약에 0이 반환됐으면 min때문에 거리두기 flag는 무조건 0 됨
                        # flag = 1일 조건) 모든 사람들이 다 거리두기 지켜야됨
        answer.append(flag) # 최종 거리두기 flag push
    return answer

places = [["XPOOX", "PXOXO", "OOOOO", "OOOOO", "OOOOO"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))