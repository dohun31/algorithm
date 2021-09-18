def add_member(dict, a, b):
    if dict.get(a, 0):
        if len(dict[a]) < m:
            dict[a].append(b)
    else:
        dict[a] = [b]

def print_member(dict):
    for key, value in sorted(dict.items(), key = lambda x: x[0]):
        for v in sorted(value, key = lambda x: (len(x), x)):
            print(key, v)

if __name__ == "__main__":
    n, m = map(int, input().split())
    odd, even = {}, {}

    while True:
        a, b = input().split()
        if a == b == "0":
            break
        a = int(a)
        if a % 2 == 0: add_member(even, a, b)
        else: add_member(odd, a, b)

    print_member(odd)
    print_member(even)