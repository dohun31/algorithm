if __name__ == "__main__":
    from collections import defaultdict

    k, n, f = map(int, input().split())
    friends = defaultdict(list)

    for _ in range(f):
        f1, f2 = map(int, input().split())
        if f2 not in friends[f1]:
            friends[f1].append(f2)
            friends[f2].append(f1)
    print(sorted(friends.items(), key = lambda x: (-len(x[1]), x[0])))
    answers = sorted([key for key, _ in sorted(friends.items(), key = lambda x: (-len(x[1]), x[0]))[:k]])
    if answers:
        for answer in answers:
            print(answer)
    else:
        print(-1)