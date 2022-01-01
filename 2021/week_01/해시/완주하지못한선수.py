participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

def solution(participant, completion):
    result = {}
    for i in participant:
        result[i] = result.get(i, 0) + 1
    for i in completion:
        result[i] -= 1
    return "".join([key for key, value in result.items() if value != 0])

result = solution(participant, completion)
print(result)