import math

def solution(N, stations, W):
    sections = []
    if stations[0] - W - 1 >= 1:
        sections.append((1, stations[0] - W - 1))

    for i in range(len(stations) - 1):
        start = stations[i] + W + 1
        end = stations[i + 1] - W - 1
        if start <= end:
            sections.append((start, end))
            
    if stations[-1] + W + 1 <= N:
        sections.append((stations[-1] + W + 1, N))

    answer, possible = 0, 2 * W + 1
    for section in sections:
        lenv = section[1] - section[0] + 1
        if lenv < possible:
            answer += 1
        else:
            answer += math.ceil(lenv / possible)
            
    return answer

if __name__ == "__main__":
    N = 11
    stations = [4, 11]
    W = 1
    print(solution(N, stations, W))