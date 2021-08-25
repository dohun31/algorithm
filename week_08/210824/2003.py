n, m = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
end = 0
sum = nums[end]
for start in range(n):
    while sum < m and end < n - 1:
        end += 1
        sum += nums[end]
    if sum == m:
        cnt += 1
    sum -= nums[start]

print(cnt)
