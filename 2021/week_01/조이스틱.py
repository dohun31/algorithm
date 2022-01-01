name = input()

start = ord('A')
end = ord('Z')
max_sub = end - start + 1

def solution(name):
    max_sub = ord('Z') - ord('A') + 1
    
    name = list(map(ord, list(name)))
    name_a = [ord('A')] * len(name)
    
    result = 0
    for i in range(len(name)):
        sub = name[i] - name_a[i]
        result += min(sub, max_sub - sub)

        if i != len(name) - 1:
            result += 1
        print(result)
    return result

result = solution(name)
print(result)