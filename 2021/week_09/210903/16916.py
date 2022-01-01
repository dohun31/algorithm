def set_table(p):
    l = len(p)
    table = [0] * l
    j = 0
    for i in range(1, l):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1]
        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table

def kmp(t, p):
    lt, lp = len(t), len(p)
    table = set_table(p)
    j = 0
    for i in range(lt):
        while j > 0 and t[i] != p[j]:
            j = table[j - 1]
        if t[i] == p[j]:
            if j == lp - 1:
                return True
            else:
                j += 1
    return False

t = input()
p = input()
result = kmp(t, p)
print(1 if result else 0)