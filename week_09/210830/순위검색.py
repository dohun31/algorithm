# 정확도
def solution(info, query):
    answer = []
    info = list(map(lambda x: x.split(), info)) # list로 만들기
    for qry in query:
        # query to list
        qry = qry.split(' and ')
        qry = qry[:-1] + qry[-1].split()
        # 걸러지는 애들 저장할 list
        result = [[] for _ in range(len(qry))]
        result[0] = [i for i in range(len(info))]
        # 조건에 맞게 거르기
        for idx, qr in enumerate(qry[:-1]):
            if qr == '-':
                result[idx + 1] = result[idx] # - 라면 앞에 조건 그대로 감
            else:
                for r in result[idx]: # 앞에서 거른 애들만 탐색
                    if info[r][idx] == qr:
                        result[idx + 1].append(r)
        # 마지막 걸러진 애들 비교
        cnt = 0
        for r in result[-1]:
            if int(info[r][-1]) >= int(qry[-1]):
                cnt += 1
        answer.append(cnt)
    return answer

info = ["java backend junior pizza 150",\
        "python frontend senior chicken 210",\
        "python frontend senior chicken 150",\
        "cpp backend senior pizza 260",\
        "java backend junior chicken 80",\
        "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",\
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150"]

# 정확도 & 효율성
from itertools import combinations
import bisect

def make_all_case(info):
    case = []
    for i in range(5):
        for arr in combinations(range(4), i):
            c = ''
            for idx in range(4):
                if idx not in arr:
                    c += info[idx]
                else:
                    c += '-'
            case.append(c)
    return case

def solution1(info, query):
    answer = []
    all_case = {}
    # infomation 전처리
    for i in info:
        splited_info = i.split()
        cases = make_all_case(splited_info) # 모든 경우
        for case in cases:
            if not all_case.get(case, 0):
                all_case[case] = [int(splited_info[-1])]
            else:
                all_case[case].append(int(splited_info[-1]))
    # 점수순으로 정렬
    for key in all_case.keys():
        all_case[key].sort()
    # 쿼리 탐색
    for q in query:
        splited_query = q.split()
        target = ''.join(splited_query[::2])
        if all_case.get(target, 0):
            answer.append((len(all_case[target]) - bisect.bisect_left(all_case[target], int(splited_query[-1]))))
        else:
            answer.append(0)
    return answer

print(solution(info, query))