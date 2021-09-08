from itertools import combinations, permutations
from collections import Counter

def make_all_case(uid):
    user = []
    l = len(uid)
    for i in range(l + 1):
        for set in combinations(range(l), i):
            id = ''
            for j in range(l):
                if j not in set:
                    id += uid[j]
                else:
                    id += '*'
            user.append(id)
    return user

def check_banned(cases, banned_id):
    check = []
    for i in range(len(banned_id)):
        if banned_id[i] in cases:
            check.append(i)
    return check

def solution(user_id, banned_id):
    result = []
    all_case, banned_user = {}, list(permutations(user_id, len(banned_id)))
    
    for uid in user_id:
        cases = make_all_case(uid)
        check = check_banned(cases, banned_id)
        all_case[uid] = check
    
    for users in banned_user:
        cnt = 0
        for i in range(len(users)):
            if i not in all_case[users[i]]:
                break
            cnt += 1
        if cnt == 4:
            result.append(''.join(sorted(users)))

    return len(set(result))

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]	
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))