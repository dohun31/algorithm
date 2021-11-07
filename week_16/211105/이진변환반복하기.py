def solution(s):
    stage_answer = 0
    zero_answer = 0 
    while len(s) > 1:
        zero_count = s.count('0')
        nowv = len(s) - zero_count
        s = ''.join(list(format(nowv, 'b')))
        stage_answer += 1
        zero_answer += zero_count
    return [stage_answer, zero_answer]

if __name__ == "__main__":
    s = "110010101001"	
    print(solution(s))