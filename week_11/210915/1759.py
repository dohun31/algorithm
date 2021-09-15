def make_word(word, l, c, idx, m, j):
    # 원하는 길이가 됐을때 모음이 1개 이상이거나, 자음이 2개 이상이라면 출력
    if len(word) == l and m >= 1 and j >= 2:
        print(word)
        return
    # 조건 불충족으로 원하는 길이보다 길어지면 그만
    if len(word) > l:
        return
    # 마지막 붙은 알파벳의 다음 알파벳부터 탐색 -> 사전 순
    for i in range(idx + 1, c):
        # 모음개수, 자음개수 copy하기
        M, J = m, j
        if alpha[i] in m_um: M += 1
        else: J += 1
        make_word(word + alpha[i], l, c, i, M, J)

if __name__ == "__main__":
    l, c = map(int, input().split())
    alpha = sorted(list(input().split()))
    m_um = "aeiou" # 모음
    for i in range(c):
        m = j = 0 # 모음, 자음
        if alpha[i] in m_um: m += 1
        else: j += 1
        make_word(alpha[i], l, c, i, m, j)