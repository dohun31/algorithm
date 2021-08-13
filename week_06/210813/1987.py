import sys
from typing import get_args
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

row, col = map(int, input().split())
datas = [list(input().rstrip()) for _ in range(row)]
dict = {}

def dfs(x, y, ncnt):
    global count 
    count = max(count, ncnt)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx = dx + x
        ny = dy + y
        if 0 <= nx < row and 0 <= ny < col and not dict.get(datas[nx][ny], False):
            dict[datas[nx][ny]] = 1
            dfs(nx, ny, count + 1)
            del dict[datas[nx][ny]]

count = 0
dict[datas[0][0]] = 1
dfs(0, 0, count)
print(count)