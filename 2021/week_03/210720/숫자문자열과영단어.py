s = "one4seveneight"

def solution(s):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", 'nine']
    for i in range(len(numbers)):
        # 문자 숫자를 포함하고 있으면 replace해줌.
        s = s.replace(numbers[i], str(i))
    return int(s)

print(solution(s))