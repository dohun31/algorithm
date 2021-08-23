def solution(record):
    result, user = [], {}
    time = 0
    for rc in record:
        r = rc.split()
        if user.get(r[1], 0):
            if len(r) > 2 and user[r[1]][0] != r[2]:
                user[r[1]][0] = r[2]
            if r[0] == 'Change':
                continue
            user[r[1]].append(time)
        else:
            user[r[1]] = [r[2], time]
        result.append(r[0])
        time += 1

    for v in user.values():
        for time in v[1:]:
            if result[time] == 'Enter':
                result[time] = f"{v[0]}님이 들어왔습니다."
            else:
                result[time] = f"{v[0]}님이 나갔습니다."
    return result

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Change uid4567 Ryan","Enter uid1234 Prodo"]
print(solution(record))