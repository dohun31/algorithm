def solution(routes):
    routes.sort(key = lambda x: -x[1])
    answer = 0
    while routes:
        nowv = routes.pop()
        while routes and nowv[1] >= routes[-1][0]:
            routes.pop()
        answer += 1
    return answer

if __name__ == "__main__":
    routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
    print(solution(routes))