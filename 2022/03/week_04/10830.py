import sys
import copy

def conv(arr1, arr2):
    now_graph = [[0 for _ in range(a)] for _ in range(a)]
    for i in range(a):
        for j in range(a):
            for k in range(a):
                now_graph[i][j] += (arr1[i][k] * arr2[k][j])
            now_graph[i][j] %= 1000
    return now_graph

if __name__ == "__main__":
    a, b = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(a)]
    graph2 = copy.deepcopy(graph)
    
    for i in format(b, 'b')[::-1]:
        print(i)
        if int(i) == 0:
            graph = copy.deepcopy(conv(graph, graph))
        elif int(i) == 1:
            graph = copy.deepcopy(conv(graph, graph2))

    for g in graph:
        print(*g)