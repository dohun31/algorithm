N = int(input())
count = 0

for i in range(1, N):
    if sum(list(map(int, str(i)))) + i == N:
        count = i
        break
    
print(count)