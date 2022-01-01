import math

def get_count(zero_cnt, possible_cnt):
    if zero_cnt < possible_cnt:
        zero_cnt = possible_cnt
    return math.ceil(zero_cnt / possible_cnt)

def solution(N, stations, W):
    station = [0] * (N + 1)
    for st in stations:
        for i in range(st - W, st + W + 1):
            if 0 < i <= N: station[i] = 1
    
    answer, zero_cnt, possible_cnt = 0, 0, W * 2 + 1
    for i in range(1, N + 1):
        if not station[i]:
            zero_cnt += 1
        else:
            if zero_cnt:
                answer += get_count(zero_cnt, possible_cnt)
            zero_cnt = 0
    if zero_cnt:
        answer += get_count(zero_cnt, possible_cnt)
    return answer

if __name__ == "__main__":
    N = 11
    stations = [4, 11]
    W = 1
    print(solution(N, stations, W))