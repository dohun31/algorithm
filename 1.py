from itertools import permutations
import copy

if __name__ == "__main__":
    n = int(input())
    c = list(map(int, input().split()))
    p = [[] for _ in range(n)]
    
    for i in range(n):
        pi = int(input())
        p[i] = [list(map(int, input().split())) for _ in range(pi)]

    result = sum(c)
    for per in permutations(range(n)):
        nowv = 0
        copy_c = copy.deepcopy(c)
        for i in per:
            nowv += copy_c[i]
            for j in p[i]:
                copy_c[j[0] - 1] -= j[1]
                if copy_c[j[0] - 1] < 0:
                    copy_c[j[0] - 1] = 1
        result = min(result, nowv)
        print(result)
    print(result)