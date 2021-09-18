def conv(li, a):
    sum = 0
    for i, j in zip(nums, li):
        sum += i * int(j)
    a[sum] = True

if __name__ == "__main__":
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    m = sum(nums)
    
    a = [False] * (m + 1)
    from itertools import combinations
    for i in range(1, m + 1):
        for com in combinations(range(n), i):
            li = ""
            for i in range(n):
                if i in com:
                    li += '1'
                else: li += '0'
            conv(li, a)

    cnt = 0
    for i in range(1, m + 1):
        if not a[i]: cnt += 1
    
    print(cnt)