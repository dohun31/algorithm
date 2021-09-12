def solution(n, info):
    # 점수를 가져갈 수 있는지 확인
    def check_score(idx, n):
        if info[idx] + 1 <= n: # 점수 가져갈 수 있으면
            return True # true
        return False # 점수 못내면 false
    # 어피치랑 라이언 점수 비교
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
    
    answer, l, last_score, s = [], 11, 0, [i for i in range(11)][::-1]
    result = dict()
    for i in range(l): 
        if not check_score(i, n): # 점수 낼 수 없으면 인덱스 증가
            continue
        for j in range(i, l): # window는 i 이후부터 ~ 끝까지
            for k in range(j, l): # 하나씩 무시하기 위한 변수
                score, now_n = ([0] * i) + [info[i] + 1], n - (info[i] + 1)
                for x in range(j, l):
                    if k == x: # k == x라면 뛰어넘기
                        score.append(0) # 0으로는 채워줘야함
                        continue
                    print(x, end=' ')
                    if not check_score(x, now_n): # 점수 못낼거 같으면
                        score.append(0) # 0으로 채워줌
                    else:
                        num = info[x] + 1 # 점수 내기 가능하면 info + 1 -> 왜냐면 낮은 점수 골고루 해야되니까 +1씩만해야됨
                        score.append(num) # 점수 채워줌
                        now_n -= num # 현재 남은 화살 빼주기
                if sum(score) < n: score[-1] = n - sum(score) # 아직 화살이 남았으면 제일 낮은 점수에 쏘기
                if len(score) < l: score += [0] * (l - len(score)) # 다 채웠는데 아직 길이가 모지라면 뒤에 0으로 채우기
                now_score = compare_score(info, score, s) # 점수 계산하기
                if now_score > 0:
                    last_score = max(last_score, now_score)
                    if not result.get(now_score, 0):
                        result[now_score] = []
                    if score not in result[now_score]:
                        result[now_score].append(score)
                print()
    if last_score > 0:
        return sorted(result[last_score], key = lambda x: (x[10], x[9], x[8], x[7], x[6], x[5], x[4], x[3], x[2], x[1], x[0]))[-1]
    else:
        return [-1]

n = 1
info = [1,0,0,0,0,0,0,0,0,0,0]
print(solution(n, info))

