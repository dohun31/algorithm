def solution(new_id):
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()
    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    new_id = "".join(list(filter(lambda x: x.isalnum() or x == '-' or x == '_' or x == '.', new_id)))
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    new_id_stack = []
    for id in new_id:
        if new_id_stack and id == '.' and new_id_stack[-1] == '.':
            continue
        new_id_stack.append(id)
    new_id = "".join(new_id_stack)
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if new_id and new_id[0] == '.' : new_id = new_id[1:]
    if new_id and new_id[-1] == '.' : new_id = new_id[:-1]
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if not new_id: new_id = 'a'
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    l = len(new_id)
    if l >= 16: 
        new_id = new_id[:15]
        if new_id[-1] == '.' : new_id = new_id[:-1]
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    elif l <= 2:
        new_id += new_id[-1] * (3 - l)
    print(new_id)
    return new_id

assert solution("...!@BaT#*..y.abcdefghijklm") == "bat.y.abcdefghi"
assert solution("z-+.^.") == "z--"
assert solution("123_.def") == "123_.def"
assert solution("abcdefghijklmn.p") == "abcdefghijklmn"
assert solution("=.=") == "aaa"

