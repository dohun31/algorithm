if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    row, col, BLOCK = map(int, input().split())

    block_counter = {}
    graph = []
    for i in range(row):
        g = list(map(int, input().split()))
        for j, value in enumerate(g):
            if block_counter.get(value, 0):
                block_counter[value] += 1
            else:
                block_counter[value] = 1
        graph.append(g)
        
    all_case = list(block_counter.items())
    l = len(all_case)
    min_time = int(1e10)
    result_h = -1
    for idx, case in enumerate(all_case):
        possible_block = BLOCK
        target_h, target_cnt = case
        now_time = 0
        flag = True
        for i in range(l):
            if i != idx:
                h, cnt = all_case[i]
                if cnt <= possible_block:
                    if h < target_h:
                        now_time += (target_h - h) * cnt
                    elif h > target_h:
                        now_time += (h - target_h) * cnt * 2
                    possible_block -= cnt
                else:
                    flag = not flag
        if flag:
            if min_time > now_time:
                min_time = now_time
                result_h = target_h
            elif min_time == now_time:
                min_time = now_time
                if result_h < target_h:
                    result_h = target_h
    print(min_time, result_h)