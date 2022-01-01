def solution(s):
    string = list(s)
    for i in range(len(string)):
        if string[i].isalpha():
            if i == 0 or string[i - 1] == " ": string[i] = string[i].upper()
            else: string[i] = string[i].lower()
    return ''.join(string)

if __name__ == "__main__":
    s = "for the last week"
    print(solution(s))