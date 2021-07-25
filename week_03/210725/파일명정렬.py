def solution(files):
    input_files = []
    answer = []
    for file in files:
        head, number, tail = '', '', ''
        for f in file:
            if f.isdigit() and not tail:
                number += f
            else:
                if not number:
                    head += f
                else:
                    tail += f
        input_files.append({'head': head, 'lower-head': head.lower(),'number': number, 'tail': tail})

    for file in sorted(input_files, key=lambda x:(x['lower-head'], int(x['number']))):
        full_name_file = file['head'] + file['number'] + file['tail']
        answer.append(full_name_file)

    return answer

files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(files))