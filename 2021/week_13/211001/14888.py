if __name__ == "__main__":
    from itertools import permutations

    n = int(input())
    datas = list(map(int, input().split()))

    add = lambda a, b: a + b
    mis = lambda a, b: a - b
    mul = lambda a, b: a * b
    div = lambda a, b: a // b if a >= 0 else -((-a) // b)
    operator = []
    for op, cnt in zip([add, mis, mul, div], map(int, input().split())):
        for _ in range(cnt):
            operator.append(op)
    
    result = [-int(1e10), int(1e10)]
    for opcode in permutations(operator, n - 1):
        now_result = datas[0]
        for idx, op in enumerate(opcode):
            now_result = op(now_result, datas[idx + 1])
        result[0] = max(result[0], now_result)
        result[1] = min(result[1], now_result)

    for r in result:
        print(r)