def calculate_number(op, a, b):
    if op == '*': return a * b
    elif op == '+': return a + b
    elif op == '-': return a - b

def solution(expression):
    from itertools import permutations
    opcodes = list(permutations(['*', '+', '-']))
    exp, num, answer = [], '', 0
    for e in expression:
        if e.isdigit():
            num += e
        else:
            exp.append(num)
            exp.append(e)
            num = ''
    exp.append(num)
    for opcode in opcodes:
        now_exp = exp
        for op in opcode:
            while op in now_exp:
                op_idx = now_exp.index(op)
                a, b = int(now_exp[op_idx - 1]), int(now_exp[op_idx + 1])
                now_exp = now_exp[:op_idx - 1] + [calculate_number(op, a, b)] + now_exp[op_idx + 2:]
        answer = max(answer, abs(now_exp[-1]))
    return answer

if __name__ == "__main__":
    expression = "50*6-3*2"
    print(solution(expression))