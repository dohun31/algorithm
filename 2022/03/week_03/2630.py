import sys

def check_color(n, row, col):
    global white, blue
    cnt_blue = 0
    for i in range(row, row + n):
        cnt_blue += sum(graph[i][col:col + n])
    if cnt_blue == n * n:
        blue += 1
    elif cnt_blue == 0:
        white += 1
    else:
        n //= 2
        check_color(n, row, col)
        check_color(n, row + n, col)
        check_color(n, row, col + n)
        check_color(n, row + n, col + n)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    white, blue = 0, 0
    check_color(n, 0, 0)

    print(white)
    print(blue)