import math
from collections import deque

progresses = [95, 95, 95, 95]
speeds = [4, 3, 2, 1]

def solution(progresses, speeds):
    queue = deque([math.ceil((100 - progress) / speed) for speed, progress in zip(speeds, progresses)])
    result = [1]
    now_data = queue.popleft()
    while queue:
        if now_data >= queue[0]:
            result[-1] += 1
            queue.popleft()
        else:
            now_data = queue.popleft()
            result.append(1)
    return result

print(solution(progresses, speeds))