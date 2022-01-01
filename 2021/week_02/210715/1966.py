from collections import deque
import sys

N = int(input())

for _ in range(N):
    n, target = map(int, sys.stdin.readline().split())
    datas = list(map(int, sys.stdin.readline().split()))
    queue = []
    result = 1
    # datas를 [data, index]형태로 바꿈
    for i, data in enumerate(datas):
        queue.append([data, i])
    queue = deque(queue)
    datas.sort()

    while queue:
        data = queue.popleft() 
        # index가 target이랑 같을 떄
        if data[1] == target:
            # data값이 max값이면(중요도가 제일 높으면)
            if data[0] == datas[-1]:
                print(result)
                break
            else:
                queue.append(data)
        else:
            # data가 max값이면 datas의 max값을 pop해 줌
            if data[0] == datas[-1]:
                result += 1
                datas.pop()
            else: # 다시 큐에 넣어줌
                queue.append(data)
                