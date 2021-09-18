def signal(i, j):
    no_signal[i][0] = "*"
    no_signal[i][j + 1] = "*"
    no_signal[i][-(j + 2)] = "*"
    no_signal[i][-1] = "*"

if __name__ == "__main__":
    n = int(input())
    no_signal = [[" " for _ in range(n)] for _ in range(n)]
    no_signal[0] = no_signal[-1] = ['*'] * n

    middle = n // 2 + 1 if n % 2 == 0 else n // 2
    j = 0
    for i in range(1, middle):
        signal(i, j)
        j += 1
    
    j = j - 3 if n % 2 == 0 else j
    for i in range(middle , n - 1):
        signal(i, j)
        j -= 1
    
    for sig in no_signal:
        print(''.join(sig))