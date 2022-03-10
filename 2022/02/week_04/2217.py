if __name__ == "__main__":
    import sys
    arr = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
    max, l = 0, len(arr)
    for idx, nowv in enumerate(sorted(arr)):
        if max < nowv * (l - idx):
            max = nowv * (l - idx)
    print(max)