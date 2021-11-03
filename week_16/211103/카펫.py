import math

def solution(brown, yellow):
    number = []
    sumv = brown + yellow
    for i in range(3, int(math.sqrt(sumv)) + 1):
        if sumv % i == 0:
            number.append(i)
            number.append(sumv // i)
    number.sort()
    for i in range(len(number) // 2):
        BH, BW = number[i], number[-(i + 1)]
        if (BH - 2) * (BW - 2) == yellow:
            return [BW, BH]

if __name__ == "__main__":
    brown = 24
    yellow = 24
    print(solution(brown, yellow))