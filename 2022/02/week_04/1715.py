if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())
    arr = sorted([int(sys.stdin.readline()) for _ in range(n)])
    if len(arr) <= 2:
        print(sum(arr))
    else:
        acc = sum(arr[:2])
        sumv = acc
        l = len(arr)
        for i in range(2, l):
            print(acc, arr[i])
            sumv += acc + arr[i]
            acc += arr[i]
        print(sumv)

# 놓친거 -> 더하면 현재 arr보다 값이 더 커질 수 있는데 더할때마다 정렬해줘야함 -> 힙 쓰기