import sys

def divide_and_conquer(size, d, r, c, cnt):
    if size == 1:
        print(cnt)
        return

    size, d = size // 4, d // 2

    if row < r + d:
        if col < c + d: 
            divide_and_conquer(size, d, r, c, cnt + size * 0) # 2사분면
        else: 
            divide_and_conquer(size, d, r, c + d, cnt + size * 1) # 1사분면
    else:
        if col < c + d: 
            divide_and_conquer(size, d, r + d, c, cnt + size * 2) # 3사분면
        else: 
            divide_and_conquer(size, d, r + d, c + d, cnt + size * 3) # 4사분면

if __name__ == "__main__":
    n, row, col = map(int, sys.stdin.readline().split())

    divide_and_conquer(4 ** n, 2 ** n, 0, 0, 0)
