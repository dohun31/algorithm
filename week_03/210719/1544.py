import sys
N = int(sys.stdin.readline().rstrip())
dict = {} # 딕셔너리 !

for _ in range(N):
    data = sys.stdin.readline().rstrip() # 문자를 받고
    flag = False
    for key in list(dict.keys()): # 딕셔너리의 key들을 탐색
        # 만약에 순환된 문자열이라면! 2개를 합친거 안에 무조건 있음
        # ex) 문자열 이랑 자열문 을 비교, 자열문 + 자열문 = 자열문자열문 에는 무조건 문자열 포함!
        # key와 문자열 길이가 같을 때 만 비교!
        if len(key) == len(data) and (key in data * 2):
            flag = True
            break
    # flag가 False일때 만 딕셔너리에 넣어줌
    if not flag:
        dict[data] = True

print(len(dict))