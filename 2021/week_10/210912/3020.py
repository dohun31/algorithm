import sys
input = sys.stdin.readline

n, h = map(int, input().split())

down_up = [0] * (h + 1) # 아래에서 위로
up_down = [0] * (h + 1) # 위에서 아래로
for i in range(n):
    num = int(input())
    if i % 2: up_down[num] += 1
    else: down_up[num] += 1

for i in range(h - 1, 0, -1):
    down_up[i] += down_up[i + 1]
    up_down[i] += up_down[i + 1]

min_num, min_cnt = 0, n
for i in range(1, h + 1):
    if min_cnt > down_up[i] + up_down[h - (i - 1)]:
        min_cnt = down_up[i] + up_down[h - (i - 1)]
        min_num = 1
    elif min_cnt == down_up[i] + up_down[h - (i - 1)]:
        min_num += 1

print(min_cnt, min_num)