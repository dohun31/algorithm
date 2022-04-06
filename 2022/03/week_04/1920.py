if __name__ == "__main__":
    my_num = {}

    n = int(input())
    for num in list(map(int, input().split())):
        my_num.setdefault(num, 1)
    
    n = int(input())
    for num in list(map(int, input().split())):
        print(my_num.get(num, 0))