from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        for w in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(w))
    return sorted(words).index(word) + 1

print(solution("I"))