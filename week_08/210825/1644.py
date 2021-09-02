import math

n = int(input())
a = [False,False] + [True] * (n-1)
primes=[]

for i in range(2, int(math.sqrt(n))+1):
    if a[i] == True:
        for j in range(2 * i , n + 1, i):
            a[j] = False

for i in range(len(a)):
    if a[i]:
        primes.append(i)

end = 0
cnt = 0
if primes:
    sum = primes[0]
    for start in range(len(primes)):
        while sum < n and end < len(primes) - 1:
            end += 1
            sum += primes[end]
        if sum == n:
            cnt += 1
        sum -= primes[start]

print(cnt)