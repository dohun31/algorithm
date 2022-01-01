def permutation(arr):
    if len(arr) == n:
        print(*arr)
        return
    for i in range(1, n + 1):
        if i not in arr:
            permutation(arr[:] + [i])

if __name__ == "__main__":
    n = int(input())
    permutation([])