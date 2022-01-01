import sys
N = int(sys.stdin.readline())
user = {}

for i in range(N):
    name, state = sys.stdin.readline().rstrip().split()
    if state == 'leave':
        del user[name]
    else:
        user[name] = state

for key in sorted(user.keys(), reverse = True):
    print(key)