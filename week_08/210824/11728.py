n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = []
a_idx, b_idx = 0, 0
while a_idx < len(a) and b_idx < len(b):
    if a[a_idx] <= b[b_idx]:
        result.append(a[a_idx])
        a_idx += 1
    else:
        result.append(b[b_idx])
        b_idx += 1

if a_idx < len(a):
    while a_idx < len(a):
        result.append(a[a_idx])
        a_idx += 1
else:
    while b_idx < len(b):
        result.append(b[b_idx])
        b_idx += 1

print(*result)

# 내장 함수 사용
print(*sorted(a + b))