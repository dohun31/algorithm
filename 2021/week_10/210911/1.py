def solution(id_list, report, k):
    from collections import Counter
    users, ban_users, last = dict(), [], ''
    for r in sorted(report):
        if last and last == r:
            continue
        last = r
        a, b = r.split()
        if users.get(a, 0):
            users[a].append(b)
        else:
            users[a] = [b]
        ban_users.append(b)
    # ban_users세기
    final_ban_users = []
    for key, cnt in Counter(ban_users).items():
        if cnt >= k:
            final_ban_users.append(key)
    # 최종
    result = []
    for i in id_list:
        if users.get(i, 0):
            cnt = 0
            for j in final_ban_users:
                if j in users[i]:
                    cnt += 1
            result.append(cnt)
        else:
            result.append(0)

    return result


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))