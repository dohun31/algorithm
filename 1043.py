import sys
from collections import deque

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    truth = list(map(int, sys.stdin.readline().split()))[1:]
    all_party = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

    q = deque(truth)
    possible = [True] * m
    visited = [False] * n

    while q:
        nowv = q.popleft()
        visited[nowv - 1] = True
        for idx, party[1:] in enumerate(all_party):
            if not possible[idx]: continue
            if nowv in party:
                possible[idx] = False
                for person in party:
                    if not visited[person - 1] and person not in q:
                        q.append(person)
    print(possible.count(True))