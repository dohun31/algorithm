import sys
input = sys.stdin.readline

n = int(input())
e = list(map(int, input().split()))
v = list(map(int, input().split()))

lesser = 0
accumulate_sum = e[0]
result_sum = 0

for i in range(1, n - 1):
    if v[lesser] >= v[i]: # 지금까지 제일 작은 기름값보다 현재 기름값이 더 작다면
        result_sum += v[lesser] * accumulate_sum # 누적된 거리만큼 지금까지 제일 작았던 기름값으로 결제 -> 현재 기름값으론 이전 거리는 계산 못함
        lesser = i # 제일 작은 기름값의 위치를 기억
        accumulate_sum = e[i] # 누적된 거리를 다음 거리로 초기화
    else:
        accumulate_sum += e[i] # 지금까지 제일 작은 기름값이 계속해서 작다면 거리를 누적함

if accumulate_sum != 0: # 반복문이 끝났는데도 누적된 거리가 남아있다면
    result_sum += v[lesser] * accumulate_sum # 결제 마무리 하고 끝냄.

print(result_sum)