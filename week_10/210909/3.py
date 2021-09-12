def solution(a, b, g, s, w, t):
    answer = 0
    gold_city = []
    sliver_city = []
    for i in zip(g, s, w, t):
        if i[0] != 0:
            gold_city.append(i)
        if i[1] != 0:
            sliver_city.append(i)
    gold_city.sort(key=lambda x: x[3])
    sliver_city.sort(key=lambda x: x[3])
    
    print(gold_city, sliver_city)

a, b, g, s, w, t = 90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]
print(solution(a, b, g, s, w, t))