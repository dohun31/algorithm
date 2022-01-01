def solution(n, info):
    all_case = []
    def bfs(n, now_n, arr):
        if len(arr) == 11:
            all_case.append(arr)
            return
        if now_n == 0:
            bfs(n, now_n, arr + [0])
        else:
            bfs(n, now_n - 1, arr + [1])
            bfs(n, now_n, arr + [0])
    def make_all_score(case):
        now_n, arr = n, []
        for i in range(11):
            if case[i] == 1:
                if info[i] + 1 <= now_n:
                    arr.append(info[i] + 1)
                    now_n -= (info[i] + 1)
                    continue
            arr.append(0)
        if now_n > 0: arr[-1] = now_n
        return arr
    def compare_score(apch, lion, s):
        apch_s, lion_s = 0, 0 # 0으로 초기화
        for idx, (ap, li) in enumerate(zip(apch, lion)): # 점수 내기 위한 idx랑 ap, li점수 맞춘개수
            if ap > li: # 어피치가 더 많이 맞추면
                apch_s += s[idx] # 어피치 점수
            elif ap < li: # 라이언이 더 많이 맞추면
                lion_s += s[idx] #라이언 점수
            else: # 같은 경우
                if ap == li ==  0: # 둘 다 0이라면
                    continue # 점수는 아무도 없음
                else:
                    apch_s += s[idx] # 0이 아니고 같다면 어피치 점수
        return lion_s - apch_s if lion_s > apch_s else -1 # 라이언 점수가 더 크다면 점수 격차 전달 아니라면 0
    bfs(n, n, [0])
    bfs(n, n - 1, [1])
    all_score = []
    for case in all_case:
        all_score.append(make_all_score(case))
    s = [i for i in range(11)][::-1]
    all_result = {}
    for score in all_score:
        now_score = compare_score(info, score, s)
        if now_score > 0:
            if all_result.get(now_score, 0): all_result[now_score].append(score)
            else: all_result[now_score] = [score]
    max_score = max(all_result.keys())
    result = []
    for score in all_result[max_score]:
        result.append(''.join(list(map(str, score))))
    result = set(result)
    print(result)


print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))