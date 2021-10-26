def solution(n, words):
    target = cnt = 0
    for i in range(1, len(words)):
        # 탈락 조건 
        # 1. 현재 단어의 첫번째 알파벳이랑, 이전 단어의 마지막 알파벳이랑 다를 경우
        # 2. 이전에 나왔던 단어일 경우
        # 3. 한 글자 단어일 경우
        if words[i][0] != words[i - 1][-1] or words.index(words[i]) != i or len(words[i]) == 1:
            target, cnt = (i % n) + 1, (i // n) + 1
            break
    return [target, cnt]


if __name__ == "__main__":
    n = 2
    words = ["hello", "one", "even", "never", "now", "world", "draw"]
    print(solution(n, words))