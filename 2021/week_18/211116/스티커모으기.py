def solution(sticker):
    even, odd = 0, 0
    for i in range(0, len(sticker)):
        if i % 2 == 0: even += sticker[i]
        else: odd += sticker[i]
    if len(sticker) % 2 == 1:
        even -= min(sticker[0], sticker[-1])
    return max(even, odd)

if __name__ == "__main__":
    sticker = [1, 3, 2, 5, 4]
    print(solution(sticker))