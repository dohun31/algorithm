def make_table(s):
    result = 0
    for k in range(len(s)):
        ss = s[k:]
        l = len(ss)
        table = [0] * l
        j = 0
        for i in range(1, l):
            while j > k and ss[i] != ss[j]:
                j = table[j - 1]
            if ss[i] == ss[j]:
                j += 1
                table[i] = j
        result = max(result, max(table))
    return result

s = input()

print(make_table(s))

