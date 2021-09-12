directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(board, aloc, bloc):
    last_a, last_b = aloc, bloc
    def simulation(state):
        def go_a():
            for dx, dy in directions:
                x, y = last_a[0], last_a[1]
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col:
                    last_a = [nx, ny]
                    simulation(1)
        def go_b():
            for dx, dy in directions:
                x, y = last_b[0], last_b[1]
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col:
                    last_b = [nx, ny]
                    simulation(0)
        if state == 0:
            go_a()
        else:
            go_b()
    row, col = len(board), len(board[0])
    for dx, dy in directions:
        visited = [[0 for _ in range(col)] for _ in range(row)]
        simulation(x + dx, y + dy)
    return 1

board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]
print(solution(board, aloc, bloc))