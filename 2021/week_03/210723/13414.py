import sys
K, L = map(int, sys.stdin.readline().split())
students = {}

for i in range(L):
    student = sys.stdin.readline().rstrip()
    students[student] = i # 새로 들어올때마다 순서 갱신

# 들어온 순서대로 정렬해줌
result = sorted(students.items(), key = lambda x: x[1]) 

if K > len(result): # 정원 수 보다 신청 학생 수가 더 적으면
    K = len(result) # K는 신청한 사람 수
for i in range(K): 
    print(result[i][0]) # 들어온 순서대로 수강 신청 성공