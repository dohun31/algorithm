import sys
N = int(sys.stdin.readline())
peoples = []

for _ in range(N):
    people = sys.stdin.readline().split()
    peoples.append(people)

peoples.sort(key = lambda x: (int(x[0])))

for age, name in peoples:
    print(age, name)