def conv_alpha(words, alpha):
    for word in words:
        l = len(word) - 1
        for w in word:
            alpha[w] += 10 ** l
            l -= 1

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    # 입력받을 단어의 수
    n = int(input())
    # n개의 단어를 저장할 변수
    words = [input().rstrip() for _ in range(n)]
    # 알파벳들의 가중치를 계산할 dict자료형
    alpha = {}
    for i in range(26):
        alpha.setdefault(chr(i + 65), 0)
    # 알파벳 가중치 계산하기
    conv_alpha(words, alpha)
    # 가중치가 0이상인 알파벳들만 filterling하고 알파벳순, 점수순으로 sort하기
    positive_alpha = sorted(list(filter(lambda x: x[1] > 0, alpha.items())), key = lambda x:(-x[1], x[0]))
    # 숫자 만들기
    j, sum = 9, 0
    for i in range(len(positive_alpha)):
        sum += j * positive_alpha[i][1]
        if j > 0:
            j -= 1
    
    print(sum)