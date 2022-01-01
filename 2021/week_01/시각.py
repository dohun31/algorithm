# 정수 N 입력
N = int(input())

times = [N + 1, 60, 60]

result = 1

# 이렇게 하면 시간 분 초에 모두 3이 포함 될때가 세어짐
# for time in times:
#     cnt = 0
#     for i in range(time):
#         if '3' in str(i):
#             print(i)
#     if cnt != 0: result *= cnt

# 시 분 초 같이 합쳐서 계산해야됨
cnt = 0
for i in range(times[0]):
    for j in range(times[1]):
        for k in range(times[2]):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)