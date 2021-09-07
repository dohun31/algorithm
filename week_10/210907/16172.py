import sys
input = sys.stdin.readline

s = input().rstrip()
k = input().rstrip()

def make_table(s):
    l, j = len(s), 0
    table = [0] * l
    for i in range(1, l):
        while j > 0 and s[i] != s[j]:
            j = table[j - 1]
        if s[i] == s[j]:
            j += 1
            table[i] = j
    return table

def solution(s, k):
    ls, lk, table = len(s), len(k), make_table(k)
    j = 0
    for i in range(ls):
        print(s[i], k[j])
        if s[i].isdigit():
            continue
        while j > 0 and s[i] != k[j]:
            j = table[j - 1]
        if s[i] == k[j]:
            j += 1
        if j == lk:
            return 1
    return 0

print(solution(s, k))