n, s = map(int, input().split())
nums = list(map(int, input().split()))

end = 0
sum = nums[end]
result = []

for start in range(n):
    # 가능한만큼 end슬라이딩 하기
    while sum < s and end < n - 1:
        end += 1
        sum += nums[end]
    # 만약에 sum이 s랑 같으면 기억
    if sum >= s:
        result.append(end - start + 1)
    # start슬라이딩 하기 - num[start]만큼 빼기
    sum -= nums[start]

print(min(result)) if result else print(0)