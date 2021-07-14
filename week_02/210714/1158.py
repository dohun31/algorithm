from collections import deque

N, K = map(int, input().split())
queue = [i for i in range(1, N + 1)] # queue에는 1~N까지 정수가 담김
result = [] # 결과를 저장 할 변수

queue = deque(queue)

i = 1
while queue :
    data = queue.popleft()
    if i == K: # K번쨰에 앉은 사람이라면
        result.append(str(data)) # result에 push
        i = 1
    else: # K번째에 앉은 사람이 아니라면
        queue.append(str(data)) # 다시 큐에 들어감
        i += 1 

print('<' + ", ".join(result) + '>')
