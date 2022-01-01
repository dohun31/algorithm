# 정수 N을 입력받는다
N = int(input())
# N개의 정수를 입력받음
array = list(map(int, input().split()))

# 오름차순으로 정렬
array.sort()

count = 0 # 모험가 수 세기
result = 0 # 모험가 그룹 수 세기

for i in array:
    count += 1 # 모험가끼리 뭉치는데
    if count >= i: # 모험도 이상만큼 뭉치면
        result += 1 # 그룹 수 +1 해주고
        count = 0 # 다시 모험가 뭉침

print(result)
