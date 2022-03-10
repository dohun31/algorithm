import sys

if __name__ == "__main__":
    m = int(sys.stdin.readline())
    my_set = {}

    for _ in range(m):
        command = sys.stdin.readline().rstrip().split()
        if command[0] == "add":
            my_set += int(command[1])
        print(my_set)
