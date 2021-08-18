import sys
input = sys.stdin.readline

n = int(input())
words = []
max_l = 0
for _ in range(n):
    words.append(input().rstrip())
    max_l = max(max_l, len(words[-1]))

weight = [0] * 26

for i in range(len(words)):
    words[i] = words[i].zfill(max_l)

cnt = 9
sum = 0
for i, word in enumerate(zip(*words)):
    num_10 = max_l - i - 1 # 10 ^ num_10
    for w in word:
        if w != '0':
            w_int = ord(w) - 65
            if weight[w_int] == 0:
                weight[w_int] = cnt
                cnt -= 1
            sum += weight[w_int] * (10 ** num_10)
print(sum)