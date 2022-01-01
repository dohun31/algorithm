def solution(idx):
    if idx == -1:
        return True
    for i in range(-10, 11):
        answer[idx] = i
        flag = True
        for j in range(idx, n):
            nows = sum(answer[idx:j + 1])
            nowv = s[idx][j]
            if nows > 0:
                if nowv != '+':
                    flag = False
                    break
            elif nows == 0:
                if nowv != '0':
                    flag = False
                    break
            else:
                if nowv != '-':
                    flag = False
                    break
        if flag: 
            if solution(idx - 1):
                return True

if __name__ == "__main__":
    n = int(input())
    data = list(input())

    s = [[' ' for _ in range(n)] for _ in range(n)]
    start = 0
    for i in range(n):
        for j in range(i, n):
            s[i][j] = data.pop(0)
    
    answer = [0 for _ in range(n)]
    solution(n - 1)
    print(*answer)