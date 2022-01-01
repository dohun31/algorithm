def solution(s):
    my_str = []
    for c in s:
        if my_str:
            if my_str[-1] == c:
                my_str.pop()
            else:
                my_str.append(c)
        else:
            my_str.append(c)
    return 0 if my_str else 1

if __name__ == "__main__":
    s = "baabaa"
    print(solution(s))