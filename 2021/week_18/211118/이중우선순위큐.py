def solution(operations):
    from collections import deque
    q = []
    for operation in operations:
        if q: q = deque(sorted(q, key = lambda x: int(x)))
        op, num = operation.split(" ")
        if op == 'I': q.append(num)
        else:
            if q:
                if num == '1': q.pop()
                else: q.popleft()
    return [int(q[-1]), int(q[0])] if q else [0, 0]

if __name__ == "__main__":
    operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    print(solution(operations))