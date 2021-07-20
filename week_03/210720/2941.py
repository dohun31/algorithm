import sys

coatia_data = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
data = sys.stdin.readline().rstrip()
result = 0

for c_data in coatia_data:
    result += data.count(c_data)
    data = data.replace(c_data, ' ') 
    # 한 번 count한것들은 없애줌 -> dz=가 dz보다 우선순위 위 이므로 살려놓으면 뒤에서 다시 셈
    # 그리고 ''말고 ' '(공백)으로 해야됨
    # 반례) nljj -> n'lj'j -> nj -> 'nj' : count = 2 / 정답 : 3

print(result + len(data.replace(' ', ''))) # count된 애들 + 남아있는 앏파벳