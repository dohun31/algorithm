if __name__ == "__main__":
    e, s, m = map(int, input().split())

    result = 1
    start_e, start_s, start_m = 1, 1, 1
    while (start_e, start_s, start_m) != (e, s, m):
        start_e = start_e + 1 if start_e < 15 else 1
        start_s = start_s + 1 if start_s < 28 else 1
        start_m = start_m + 1 if start_m < 19 else 1
        result += 1
    print(result)