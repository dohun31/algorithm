from collections import deque
def solution(rows, colums, queries):
    num = 1
    graph = [[0 for _ in range(colums)] for _ in range(rows)]
    for i in range(rows):
        for j in range(colums):
            graph[i][j] = num
            num += 1
    answer = []
    for query in queries:
        stack = deque()
        x1, y1, x2, y2 = query
        for col in range(y1 - 1, y2 - 1):
            stack.append(graph[x1 - 1][col])
        for row in range(x1 - 1, x2 - 1):
            stack.append(graph[row][y2 - 1])
        for col in range(y2 - 1, y1 - 1, -1):
            stack.append(graph[x2 - 1][col])
        for row in range(x2 - 1, x1 - 1, -1):
            stack.append(graph[row][y1 - 1])
        answer.append(min(stack))
        for col in range(y1, y2 - 1):
            graph[x1 - 1][col] = stack.popleft()
        for row in range(x1 - 1, x2 - 1):
            graph[row][y2 - 1] = stack.popleft()
        for col in range(y2 - 1, y1 - 1, -1):
            graph[x2 - 1][col] = stack.popleft()
        for row in range(x2 - 1, x1 - 2, -1):
            graph[row][y1 - 1] = stack.popleft()
    return answer

if __name__ == "__main__":
    rows = 100
    colums = 97
    queries = [[1,1,100,97]]	
    print(solution(rows, colums, queries))