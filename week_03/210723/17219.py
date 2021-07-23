import sys
N, M = map(int, sys.stdin.readline().split())
user = {}

for _ in range(N):
    site, password = sys.stdin.readline().split()
    user[site] = password # key는 site, value는 password로 해줌.

for _ in range(M):
    search = sys.stdin.readline().rstrip()
    print(user[search]) # 찾고 싶은 site의 비밀번호를 찾아줌.